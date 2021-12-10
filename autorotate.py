import os
import subprocess

inp = subprocess.run(["dbus-send", "--system", "--dest=net.hadess.SensorProxy", "--print-reply", "/net/hadess/SensorProxy", "org.freedesktop.DBus.Properties.Get", "string:net.hadess.SensorProxy", "string:AccelerometerOrientation"], stdout=subprocess.PIPE, text=True)

out = inp.stdout.split("variant")[1].split("string ")[1].strip().replace("\"", "")

print(out)

orientation = "normal"
if out == "left-up":
    orientation = "left"
elif out == "right-up":
    orientation = "right"
elif out == "bottom-up":
    orientation = "inverted-y"

print(orientation)

subprocess.run(["./gnome-randr.py", "--output", "eDP-1", "--rotate", orientation])
