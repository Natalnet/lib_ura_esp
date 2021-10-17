# Complete project details at https://RandomNerdTutorials.com

import time
from umqttsimple import MQTTClient
import ubinascii
import machine
import network
import esp
esp.osdebug(None)
import gc
gc.collect()

import json 
conf_file = open('conf.json') 
conf = json.load(conf_file) 
conf_file.close() 

# Robot codes 
from L9110URA import L9110URA
robot = L9110URA(13,12,5,23)

from hcsr04 import HCSR04
 
distSensor = HCSR04(trigger_pin=19, echo_pin=18)

leftLineSensor =  machine.Pin(14, machine.Pin.IN,  machine.Pin.PULL_UP)
rightLineSensor =  machine.Pin(27, machine.Pin.IN,  machine.Pin.PULL_UP)


ssid = conf["ssid"]
password = conf["password"]
mqtt_server = conf["mqtt_server"]
server_port = conf["server_port"] 
mqtt_user = conf["mqtt_user"]
mqtt_password = conf["mqtt_password"]

client_id = ubinascii.hexlify(machine.unique_id())
topic_sub = b'URA01/input'
topic_pub = b'URA01/output'

last_message = 0
message_interval = 1
counter = 0

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())







