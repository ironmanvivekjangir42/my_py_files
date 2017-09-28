#!/usr/bin/python3
import os#importing os libraries
import time#importing time libraries
a=0
b=1
while a<=10:#create a while loop
    im=str(b)+".jpg"#creating a int to string
    img="/home/pi/camm/imgs/"
    cmd= "fswebcam -F 5 --fps 20 -r \"1200x800\" "+img
    t=cmd+im#command
    os.system(t)#execute the command
    a=a+1
    b=b+1
    time.sleep(30)#add a delay of 30 seconds
