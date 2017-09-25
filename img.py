#!/usr/bin/python3
import os
import time
a=0
b=1
while a<=10:

    t="fswebcam -F 5 --fps 20 -r \"1200x800\" /home/pi/cam/imgs/"+str(b)+".jpg"
    os.system(t)
    print(b)
    a=a+1
    b=b+1
    time.sleep(30)