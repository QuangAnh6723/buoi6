# khai bao thu vien
import paho.mqtt.client as mqtt
import json
# from grove.grove_relay import GroveRelay
# from gpiozero import LED

# khai bao chan
# led=LED(22)
# relay=GroveRelay(5)

#khai bao cho mqtt
client_id = 'JTI2AA8YAwIhEykYLigRIRg'
username_mqtt = 'JTI2AA8YAwIhEykYLigRIRg'
password_mqtt = 'BqwslLtG9rX51U+p5bHDMGYY'

# tao bien global de luu cac gia tri
mode = 0
led_state = 0
relay_state = 0
humi = 90
temp = 25

def dieu_khien():
    if mode == 1: # che do manual
    # kiem tra led
        print("mode manual")
        if led_state == 1:
            # led.on()
            print("led on")
        elif led_state == 0:
            # led.off()
            print("led off")
        if relay_state == 1: 
            # relay.on()
            print("relay on")
        elif relay_state == 0:
            # relay.off()
            print("relay off")
    elif mode == 0:  # mode auto
        print("mode auto")      
        if temp > 35:
            # led.on()
            print("led on")
        elif temp < 31:
            # led.off()
            print("led off")
        if humi > 90:
            relay.on()
            # print("relay on")
        elif humi < 60:
            relay.off()
            # print("relay off")

def on_connect(client, userdata,flags,rc):
    channel_ID = "2287342"
    print("Connected with result code {}".format(rc))
    client.subscribe('channels/'+channel_ID+'/subscribe')
    
def on_disconnect(client,userdata,rc):
    print("Disconnected from Broker")

def on_message(client, userdata, message):
    print('debug')
    
    global mode, led_state, relay_state,humi,temp
    fields = message.payload.decode()
    fields = message.payload.decode()
    fields = json.loads(str(fields))

    if fields['field3'] != None:  # check mode
        mode = int(fields['field3'])
        print('mode: ', mode)

    if fields['field4'] != None:  # check led_state
        led_state = int(fields['field4'])
        print('led state: ', led_state)

    if fields['field5'] != None:  # check relay_state
        relay_state = int(fields['field5'])
        print('relay state: ', relay_state)
    
    if fields['field2'] != None:  # check humi
        humi = int(fields['field2'])
        print('humi: ', humi)

    if fields['field1'] != None:  # check temp
        temp = int(fields['field1'])
        print('temp: ', temp)
    
    print(humi, temp)
    dieu_khien()
    print('=========================================')
# ========================================================================

client = mqtt.Client(client_id)

# gan cac chuong trinh con
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_message
client.username_pw_set(username= username_mqtt, password= password_mqtt)
client.connect("mqtt3.thingspeak.com", 1883,60)
client.loop_forever()
        