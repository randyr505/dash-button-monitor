import socket
import struct
import binascii
import os
import ConfigParser
from itertools import chain

dir_name = os.path.dirname(os.path.realpath(__file__))
conf = dir_name + '/dash_monitor.cf'
process_button = dir_name + '/scripts/process_button.sh'

config = ConfigParser.ConfigParser()
config.read(conf)
rawSocket = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(0x0003))

dashes = config.items('dashes')
exclude_macs = config.items('exclude_macs')

while True:
  packet = rawSocket.recvfrom(2048)
  ethernet_header = packet[0][0:14]
  ethernet_detailed = struct.unpack("!6s6s2s", ethernet_header)
  arp_header = packet[0][14:42]
  arp_detailed = struct.unpack("2s2s1s1s2s6s4s6s4s", arp_header)
  ethertype = ethernet_detailed[2] 
  # skip non-ARP packets
  if ethertype != '\x08\x06':
    continue
  matched_source = False
  source_mac = binascii.hexlify(arp_detailed[5])
  dest_ip = socket.inet_ntoa(arp_detailed[8])

  for (dash_name,dash_mac) in dashes:
    if source_mac == dash_mac:
      os.system(process_button + " %s %s %s" % (dash_name, dest_ip, source_mac))
      matched_source = True
      
  if matched_source == False:
    if source_mac not in chain(*exclude_macs):
      print "Other arp request, IP = " + dest_ip + " and mac = " + source_mac
