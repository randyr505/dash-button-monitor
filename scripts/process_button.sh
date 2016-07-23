#!/bin/sh
dir=`dirname $0`
name="$1"
dest_ip="$2"
mac="$3"

date
case $name in
  #Milk|Stacys|Downy|"Red Bull"|Mucinex|Gatorade|Energizer) echo "~~~ $name button pressed, IP = $dest_ip and mac = $mac" ;;
  milk) echo "~~~ $name button pressed, executing ./$name.sh"; $dir/$name.sh ;;
     *) echo "~~~ $name button pressed, IP = $dest_ip and mac = $mac" ;;
esac
