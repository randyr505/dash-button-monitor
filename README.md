# monitor-dash-button
Displays mac addresses of dash buttons. Runs on a raspberry pi

I am not sure who all contributed to the arp parsing code since it was posted on medium via anonymous but I'll provide the link here. 

Medium post: 
  https://medium.com/@xtalker/hey-ted-i-got-this-working-on-my-raspi-without-all-the-scapy-overhead-thanks-to-http-e5704e4b16a9#.18n4jw26u

Original code I modified: 
  https://gist.github.com/anonymous/2d6eb47a0d531c20ed54

I added code to loop through multiple macs and print to stdout. Additionally to omit certain macs

#### Run dash_monitor to discover mac addresses
``` sh
sudo python dash_monitor.py
```

#### Start dash_monitor as a service
``` sh
sudo cp dash_monitor.startup /etc/init.d/dash_monitor
sudo update-rc.d dash_monitor defaults
```
