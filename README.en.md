# guncon3-linux-pyusb
Python script for managing the NAMCO Guncon3 gun for Linux

Based on the kernel driver provided by https://github.com/beardypig/guncon3

The script uses the libraries
python-uinput
pyusb
libevdev

# Install Prerequisites

`pip3 install python-uinput pyusb libevdev`

# Usage

You have to give permission to read uinput with
`sudo setfacl -m user:username:rw /dev/uinput`
where user is the name of the user who will handle the gun

Permissions to enable reading by usb should include the file 
`/etc/udev/rules.d/99-guncon3.rules`
with the following content:


```
SUBSYSTEM=="usb", ATTR{idVendor}=="0b9a", ATTR{idProduct}=="0800", MODE="0666", GROUP="plugdev", TAG+="uaccess", TAG+="udev-acl", SYMLINK+="guncon3%n"
KERNEL=="hidraw*", ATTRS{idVendor}=="0b9a", ATTRS{idProduct}=="0800",  MODE="0666", GROUP="plugdev", TAG+="uaccess", TAG+="udev-acl"
```
 
To run the script:

`python3 guncon3-linux-pyusb`

The calibration can be done with jstest-gtk


In ubuntu 18.04 it is not possible to calibrate the pistol only with jstest-gtk, and there is not (or I have not found) a graphic mode for this. 
For the calibration it will be necessary to make a combination with jstest-gtk and in the terminal command "evdev-joystick" in this way:

1.- Open jstest-gtk and go to the control associated with the gun and give properties

2.- After calibration

3.- With the gun pointing to the center, press to start calibration

4.- Point the gun with the ends or perimeter * of the screen (keep the gun always inside the perimeter).

5.- Accept

This will give us the minimum and maximum ranges to apply with evdev-joystick.

Before you have to know the command path for it in terminal mode, we write

`evemu-describe`

It will give you output like: 

```
Available devices:

/dev/input/event11:	4-Axis,9-Button

Select the device event number [0-11]: 
```

Therefore the path shall be `/dev/input/event11`

From here it will be written the minimum values that jstest has given

`sudo evdev-joystick --evdev /path --axis axis_number -m min_value -M max_value`
[where path, axis_number, min_value and max_value are variables]

For example, my config is:

```
sudo evdev-joystick --evdev /dev/input/event11 --axis 0 -m -26460 -M 25459
sudo evdev-joystick --evdev /dev/input/event11 --axis 1 -m 2311 -M 30440
sudo evdev-joystick --evdev /dev/input/event11 --axis 2 -m 0 -M 255
sudo evdev-joystick --evdev /dev/input/event11 --axis 3 -m 0 -M 255
sudo evdev-joystick --evdev /dev/input/event11 --axis 4 -m 0 -M 255
sudo evdev-joystick --evdev /dev/input/event11 --axis 5 -m 0 -M 255
```

I have not been able to configure it with advancemame (no documentation) but I have
been able to do it with gnome-video-arcade and the version of mame in the ubuntu repository.

Mame applies a dead zone to the command that is correctable in the following way in a terminal:

```
cd ~
cd ~/.mame
mame -cc
```

With this we create a configuration file mame.ini.
Inside the file there is an option "joystick_deadzone" which is 0.3 by default. Set it to 0.


* To calibrate with gnome-video-arcade I have captured the screen in a game and as a perimeter I used the content of the image.

* The GunCon3 has a bit that is activated when it goes out of the range of the leds go (and the back LED turns on). This is applied to the button 9 that could be used as a reload button in a game.


