import os
import time
a=0
b=1
while a<=10:
    os.system("fswebcam -F 5 --fps 20 -r \"1200x800\".jpg")
    a=a+1
    b=b+1
    time.sleep(30)
