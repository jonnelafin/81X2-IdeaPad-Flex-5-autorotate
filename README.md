# 81X2-IdeaPad-Flex-5-autorotate
A small python script to enable autorotation on the Ideapad Flex 5, which is bugged on gnome as of version 41

Only tested on wayland, on X11 the script could use randr instead of the included gnome-randr.py
# Dependencies
Linux Kernel 5.15 or greater is required to make the sensor work (alternately installing https://github.com/conqp/amd-sfh-hid-dkms could work).

[iio-sensor-proxy](https://gitlab.freedesktop.org/hadess/iio-sensor-proxy/), provided by your distro, eg. [arch](https://archlinux.org/packages/community/x86_64/iio-sensor-proxy/) or debian and ubuntu: ```sudo apt-get install -y iio-sensor-proxy```


If the sensor and the kernel driver both work correctly and iio-sensor-proxy is installed, the output of autorotate.py should look something like this:

```
normal
normal
new monitor configuration:
logical monitor 0:
x: 0 y: 0, scale: 1.0, rotation: normal, primary: yes
associated physical monitors:
	eDP-1 1920x1080@60.00103759765625

no changes made
```
If you see "undefined" instead of "normal", the sensor (or the driver) does not work.

# Files
autorotate.py sets your display orientation to match the orientation provided by your accelometer **once**. It assumes that your display is called "eDP-1", please change this to match your display, if it differs.

autorotate.sh uses ```watch``` to run the script every second (assumes autorotate.py is placed in ```~/scripts/autorotate.py```)

autorotate_headless.sh starts the autorotate.sh script headlessly using tmux (assumes the autorotate.sh is placed in ```~/scripts/autorotate.sh```)

gnome-randr.py is a modified version of [Oschowa/gnome-randr](https://gitlab.com/Oschowa/gnome-randr), allowing vertically mirrored orientations (holding the device upside-down)
