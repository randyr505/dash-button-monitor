#!/bin/sh

name="$1"
dest_ip="$2"
mac="$3"

case $name in
  Milk|Stacys|Downy|"Red Bull"|Mucinex|Gatorade|Energizer) echo "~~~ $name button pressed, IP = $dest_ip and mac = $mac" ;;
esac

