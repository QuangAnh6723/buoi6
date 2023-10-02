# ===================================
# khai bao thu vien
from time import sleep
from urllib import request
from seeed_dht import DHT
# import random as rd

# khai bao thiet bi
# dht = DHT("11",18)

# khai bao channel 
channel_ID = "2287342"


def post_http():
    api_key = "G3LP8MEPQ6UCKYQS"
    url = "https://api.thingspeak.com/update?api_key=%s&field1=%s&field2=%s" %(api_key,humi,temp)
    request.urlopen(url)
    r=request.urlopen(url)
    print("http send ok ")

while True:
    try:
        humi, temp = dht.read()
        # humi = rd.randint(60,100)
        # temp = rd.randint(20,40)
        post_http()
        sleep(20)
    except:
        print("error")
        sleep(1)