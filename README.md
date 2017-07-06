# Deluge LCD for Raspberry Pi

Python script for showing Deluge client downloading torrents on a I2C LED for Raspberry Pi.

![alt text](/pics/lcd-raspberry-pi-3.jpg)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software and how to install them

#### Set up Deluge for ThinClient Access
Before you do anything, take a moment to update and upgrade your repositories. Open a Terminal and run the following two commands, one after the other:
```
sudo apt-get update
sudo apt-get upgrade
```
Once that’s done, it’s time to begin installing the necessary components for the ThinClient setup. Enter the following commands:
```
sudo apt-get install deluged
sudo apt-get install deluge-console
```
This will download the Deluge daemon and console installation packages and run them. When prompted to continue, type Y. After Deluge has finished installing, you need to run the Deluge daemon. Enter the following commands:
```
deluged sudo pkill deluged
```
This starts the Deluge daemon (which creates a configuration file) and then shuts down the daemon. We’re going to edit that configuration file and then start it back up. Type in the following commands to first make a backup of the original configuration file and then open it for editing:
```
cp ~/.config/deluge/auth ~/.config/deluge/auth.old
nano ~/.config/deluge/auth
```
Once inside the nano text editor, you’ll need to add a line to the bottom of the configuration file with the following convention:
```
user:password:level
```
Where user is the username you want for Deluge, password is the password you want, and thelevel is 10 (the full-access/administrative level for the daemon). So for our purposes, we used pi:raspberry:10. When you’re done editing, hit Ctrl+X on your keyboard and save your changes when prompted. Then, start up the daemon and console again:
```
deluged deluge-console
```
If starting the console gives you an error code instead of nice cleanly formatted console interface, type “exit” and then make sure you’ve started up the daemon.

Once inside the console, you’ll need to make a quick configuration change. Enter the following:
```
config -s allow_remote True
config allow_remote exit
```
The commands and corresponding output will look like the screenshot below.

![alt text](/pics/console.png)

This enables remote connections to your Deluge daemon and double checks that the config variable has been set. Now it’s time to kill the daemon and restart it one more time so that the config changes take effect:
```
sudo pkill deluged deluged
```
At this point, your Deluge daemon is ready for remote access. Head to your normal PC (not the Raspberry Pi) and install the Deluge desktop program. You’ll find the installer for your operating system on the Deluge Downloads page. Once you’ve installed Deluge on your PC, run it for the first time; we need to make some quick changes.

Once launched, navigate to Preferences > Interface. Within the interface submenu, you’ll see a checkbox for “Classic Mode”. By default it is checked. Uncheck it.

![alt text](/pics/1.png)

Click OK and then restart the Deluge desktop client. This time, when Deluge starts, it will present you with the Connection Manager. Click the “Add” button and then input the IP address of the Raspberry Pi on your network, as well as the username and password you set during the earlier configuration. Leave the port at the default 58846. Click Add.

![alt text](/pics/2.png)

Back in the Connection Manager, you’ll see the entry for the Raspberry Pi; if all goes well, the indicator light will turn green like so:

![alt text](/pics/3.png)

Click Connect, and you’ll be kicked into the interface, connected to the remote machine:

![alt text](/pics/4.png)

It’s a fresh install, nary a .torrent in site, but our connection between the remote machine and the desktop client is a success!

Go ahead and configure the WebUI now (if you wish to do so), or skip down to the next step of this tutorial.

#### Set Up Deluge for WebUI Access
Configuring the WebUI is significantly faster, and allows for using some mobile apps to access Deluge. But as we mentioned before, you’ll have access to fewer features than with the full ThinClient experience. For example, ThinClient can associate .torrent files with the Deluge ThinClient for automatic transfer to the Pi, but you can’t do this with the WebUI.

First, take a moment to update and upgrade your repositories. Open a Terminal and run the following two commands, one after the other:
```
sudo apt-get update
sudo apt-get upgrade
```
Then, to install the WebUI, run the following commands. Note: If you already installed the Deluge daemon in the ThinClient section of the tutorial, skip the first command here.
```
sudo apt-get install deluged
sudo apt-get install python-mako
sudo apt-get install deluge-web deluge-web
```
This sequence installs the Deluge daemon (if you didn’t already install it in the last section), Mako (a template gallery for Python that the WebUI needs), the WebUI itself, and then starts the WebUI program.

The default port for the WebUI is 8112. If you wish to change it, run the following commands:
```
sudo pkill deluge-web
nano ~/.config/deluge/web.conf
```
This stops the WebUI and opens up the configuration file for it. Use nano to edit the line: “port”: 8112, and replace the 8112 with any port number above 1000 (as 1-1000 are reserved by the system).

Once you have the WebUI up and running, it’s time to connect to it using a web browser. You can use a browser on the Pi if you ever need to, but it’s not the most pleasant user experience and best left for emergencies. Open up a browser on your regular desktop machine and point it at the IP address of your Pi with the port you just chose (e.g. http://192.168.1.13:8112 ).

You’ll be greeted with a password prompt (the default password is “deluge”) and be immediately encouraged to change it after you enter it for the first time. After that, you’ll be able to interact with Deluge via the lightweight interface.

![alt text](/pics/5.jpg)

It’s not quite the same as the ThinClient, but it’s robust enough for light use and has the added benefit of serving as the point of connection for lots of torrent-control mobile apps.

### Installing

```
git clone https://github.com/darroyos/Deluge-LCD/
sudo chmod +x delugelcd.py
sudo chmod +x delugelcd.sh
```

## Authors

* **David Arroyo**
