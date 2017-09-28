import os
import time
from TwitterAPI import TwitterAPI
from gpiozero import MotionSensor

pir = MotionSensor(4)
b=1
CONSUMER_KEY = 'wSfHQNpBQqQH0hYMRZNx9EEzM'
CONSUMER_SECRET = 'LtX7XX7GOp0Y7r1LOXJ79ZNFdTUEQ0HVnMp9aofRgjQ1YSSVXl'
ACCESS_TOKEN_KEY = '912239966889025538-sELyQrELrG50uDffX1GyR1NKBK0V0t1'
ACCESS_TOKEN_SECRET = 'mLut3S3Q14b3vmoAXfLVNa4T56tlfOoSBuut3pKtXNUt4'
api = TwitterAPI(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)

while True:
    if pir.motion_detected:
        img="/home/pi/cam/"+str(b)+".jpg"
        cmd= "fswebcam -F 5 --fps 20 -r \"1200x800\" "+img
        os.system(cmd)
        print("pic taken")
        file = open(img, 'rb')
        data = file.read()
        r = api.request('statuses/update_with_media', {'status':'#pyTweetCMR'}, {'media[]':data})
        print(r.status_code)
        b=b+1
