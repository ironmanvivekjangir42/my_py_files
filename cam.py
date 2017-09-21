#!/usr/bin/python3
import os
import time
a=0
b=1
while a<=10:
    im=str(b)+".jpg"
    img="/home/pi/camm/imgs/"
    cmd= "fswebcam -F 5 --fps 20 -r \"1200x800\" "+img
    t=cmd+im
    os.system(t)
    a=a+1
    b=b+1
    time.sleep(30)
