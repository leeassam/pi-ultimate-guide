# Setup your Raspberry Pi in Headless Mode - No additional monitor, keyboard or mouse needed

## No extra monitor, no hdmi cable, no extra mouse or keyboard, just one laptop or computer - No Problem

If you just have a Raspberry Pi with an SD card and power adapter and want to set it up, here are the steps to follow. You can use an existing computer or laptop to get your SD card prepped. Follow the steps below.


### Step 1.

Flash your SD Card with the [latest version of Raspberry Pi OS](https://www.raspberrypi.com/software/) using [Raspberry Pi Imager](https://www.raspberrypi.com/software/) or [Etcher](https://www.balena.io/etcher/). I show how to do this in the course



### Step 2. 

Once you have your SD card flashed, insert it again into your laptop.

Open up File Explorer and you should see your SD card show up as a drive. Double click on it to open it to see the files that are on there



### Step 3.

You will need to create two files.



1. Create an empty file and just name it **ssh**. This file has no file extension. Just save it at the root top level. This file does not have to contain anything in it, it just has to be named ssh.

This file is created on the root level of the SD card (boot partition) when you first double click on the drive.



2. Create another file called **wpa_supplicant.conf** and again save this on the root top level. In this file, place the following contents. Turn on the hotspot on your phone so that could get the SSID of the network it creates or if you know the SSID of the wireless network that you want to connect to, use this. Also get the password you need to connect to your hotspot or the Wifi network. You will also need to get your Two Letter ISO Country Code to put in the file

You can get your **Country Code** here:

https://www.nationsonline.org/oneworld/country_code_list.htm

Put the following in your wpa_supplicant.conf file:


```
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=<<TWOLETTERCOUNTRYCODE>>
network={
    ssid="«your_SSID»"
    psk="«your_PSK»"
}
```

So as an example, the contents of your **wpa_supplicant.conf** file might look like:

```
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=US
network={
    ssid="Samsung Galaxy 29393"
    psk="juysjmd23"
}
```

Save the files and eject your SD Card

### Step 4

Insert your SD card into the RPi and boot it up. If you look on your hotspot network on your phone, you should see raspberry pi connected to your network. You should also be able to see the **IP address** that was assigned to the Raspberry Pi on your phone if you look at the details. If you have access to the router of your wireless network, you should be able to see the IP address assigned to your Raspberry Pi.

Windows users can try downloading [Advanced IP Scanner](https://www.advanced-ip-scanner.com/). This should show the IP addresses of the devices connected on your network.

You can also try running the following command on a terminal from a laptop connected to the same wireless network as your Raspberry Pi

```
ping raspberrypi
```

Depending on the security setup of your wireless network, you may or may not see the IP address of the ping responded. This would be the ip address of your Raspberry Pi.

### Step 5

Connect to the Raspberry Pi via SSH. Ensure that your computer or laptop is connected to the same HOTSPOT on your phone or the same wireless network.


Open the command line on your Windows machine or Terminal on your Mac and type the following

```
ssh pi@IP_Address_Of_PI 
```

eg

```
ssh pi@192.168.43.2 
```

Type in yes to accept the fingerprint if you get a prompt

For the password, enter **raspberry** and hit Enter. You should now be connected to your Raspberry Pi



### Step 6.

Make Configuration Changes

1. Enable the **VNC Server**



Type the following:

```
sudo raspi-config 
```


Navigate to the "Interfacing Options" and select **VNC**

Would you like the VNC Server to be enabled?

Select **Yes**

2. Select **Boot to Desktop**

- From the main Raspberry Pi Configuration screen select **Boot Options**
- Select **Desktop / CLI : Choose whetherto boot into a desktop environment or the command line**
- Select **Desktop Autologin Desktop GUI, automatically logged in as 'pi' user**
- Select **Ok**

3. Specify a **Screen Resolution**

- From the main Raspberry Pi Configuration screen select **Advanced Options**
-  Select **Resolution**
-  Select the resolution for your desktop/laptop monitor
    - I select **1920x1080
- Select **Ok**

Finish and **Reboot** for the changes to take effect.

### Step 7:

Install [VNC Viewer](https://www.realvnc.com/en/connect/download/viewer/) on your computer. I show you how to do this in the course in the section connecting remotely to your computer via VNC



### Step 8:

Enter the **IP address** that was assigned to your Raspberry Pi and the following

```
Username: pi

Password: raspberry
```

Accept the fingerprint prompt with yes if you get it and BOOM, you should be logged into your Pi!



Other note: You may need to change the resolution of the screen. You can do this by going to the Raspi Config Settings GUI and then changing the screen resolution options!


