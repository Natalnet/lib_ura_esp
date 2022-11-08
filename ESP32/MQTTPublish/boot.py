# Complete project details at https://RandomNerdTutorials.com

import time
from umqttsimple import MQTTClient
import ubinascii
import machine
import micropython
import network
import esp
esp.osdebug(None)
import gc
gc.collect()

import json 
conf_file = open('conf.json') 
conf = json.load(conf_file) 
conf_file.close() 


ssid = conf["ssid"]
password = conf["password"]
mqtt_server = conf["mqtt_server"]
server_port = conf["server_port"] 
mqtt_user = conf["mqtt_user"]
mqtt_password = conf["mqtt_password"]

client_id = ubinascii.hexlify(machine.unique_id())
topic_pub = b'test_mqtt/output'
 
# For the publish  topic 
counter = 0 
last_message = time.time()
message_interval = 10 




station = network.WLAN(network.STA_IF)
station.active(True)

if not station.isconnected():

  print('Connecting to Wi-Fi...')

  station.connect(ssid, password)

  while not station.isconnected():
    pass

  print('Connected to Wi-Fi: ', station.ifconfig())

  






