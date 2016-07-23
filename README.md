# dash-button-monitor
Displays mac addresses of Amazon's [dash buttons](http://amzn.to/29WG6lI). Runs on a raspberry pi

These scripts can be used to "hack" [dash buttons](http://amzn.to/29WG6lI). Although there really isn't any hacking of the buttons, these do provide a way to interrupt the connect to Amazon and make the [dash buttons](http://amzn.to/29WG6lI) do other things, in this example, print messages to the screen and eventually will run scripts based on the button pressed.

I am not sure who all contributed to the arp parsing code since it was posted on medium via anonymous but I'll provide the link here. 

Medium post: 
  https://medium.com/@xtalker/hey-ted-i-got-this-working-on-my-raspi-without-all-the-scapy-overhead-thanks-to-http-e5704e4b16a9#.18n4jw26u

Original code I modified: 
  https://gist.github.com/anonymous/2d6eb47a0d531c20ed54

I added code to loop through multiple macs and print to stdout. Additionally to omit certain macs

Follow the instructions Amazon provides to add your [dash button](http://amzn.to/29WG6lI) but don't select a product. When selecting a wifi to connect to I used my guest network so it was easier to determine which mac addresses were dash buttons. I also connected my raspberry pi to the guest network. The guest network is on a different subnet than the rest of my devices but the settings allow the network to see other devices. This code shows all arp requests so it can be a bit confusing. I like to check the mac addresses only (you only need the first 6 characters). Some show to be Amazon but others show to be either private or not found: [00:bb:3a](http://macaddress.webwat.ch/search/00:bb:3a)

Other found mac addresses owned by Amazon were as follows:
[74:c2:46](http://macaddress.webwat.ch/search/74:c2:46)
[44:65:0d](http://macaddress.webwat.ch/search/44:65:0d)
[74:75:48](http://macaddress.webwat.ch/search/74:75:48)
[f0:27:2d](http://macaddress.webwat.ch/search/f0:27:2d)

#### Run dash_monitor to discover mac addresses
``` sh
sudo python dash_monitor.py
```

#### Start dash_monitor as a service
``` sh
sudo cp dash_monitor.startup /etc/init.d/dash_monitor
sudo update-rc.d dash_monitor defaults
```

#### Update about credit
I noticed that if I don't select a product but I push the button a credit is applied to my account for when I select a subscribe and save item. It also seems as if it may do partial credits. i.e. I received a dash promotion credit for around $1 which I think was left over from an item that was a little over $3. YMMV

#### Deactivate button
After you have received your credit or you are just sure you are done with having the button connected to Amazon you can select a product when prompted, then go back and manage the button. When you select the button you should have the option to deactivate it.
WARNING: If you deactivate your button it will no longer be connected to wifi after the next push. You will have to setup the button again to use it.
