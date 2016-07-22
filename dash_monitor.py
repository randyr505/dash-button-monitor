import socket
import struct
import binascii
import os
rawSocket = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(0x0003))
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

  exclude_macs = ('801f01000000', '801f02000000')
  dashes = [["74c2460000", "Milk"], ["74c246000000", "Stacys"], ["00bb3a000000", "Downy"], ["44650d000000", "Red Bull"], ["747548000000", "Mucinex"], ["74c246000000", "Gatorade"], ["f0272d000000", "Energizer"]]

  for (dash_mac,dash_name) in dashes:
    if source_mac == dash_mac:
      #print "~~~ " + dash_name + " button pressed, IP = " + dest_ip + " and mac = " + source_mac
      bashcmd = "./scripts/process_button.sh %s %s %s" % (dash_name, dest_ip, source_mac)
      os.system(bashcmd)
      matched_source = True
      
  if matched_source == False:
    if source_mac not in exclude_macs:
      print "Other arp request, IP = " + dest_ip + " and mac = " + source_mac
