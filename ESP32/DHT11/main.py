# Complete project details at https://RandomNerdTutorials.com

# Sensor de temperatura 
from machine import Pin
from time import sleep
import dht

sensor = dht.DHT11(Pin(14))

ledPin = machine.Pin(4, machine.Pin.OUT)


def sub_cb(topic, msg):
  global topic_sub
  print((topic, msg))
  print(topic_sub)
  if topic == topic_sub and msg == b'l':
    print('ligar')
    ledPin.on()
    
  if topic == topic_sub and msg == b'd':
    print('desligar')
    ledPin.off() 


def connect_and_subscribe():
  global client_id, mqtt_server, topic_sub, server_port, mqtt_user, mqtt_password
  client = MQTTClient(client_id, mqtt_server, server_port, mqtt_user, mqtt_password)
  client.set_callback(sub_cb)
  client.connect()
  client.subscribe(topic_sub)
  print('Connected to %s MQTT broker, subscribed to %s topic' % (mqtt_server, topic_sub))
  return client

def restart_and_reconnect():
  print('Failed to connect to MQTT broker. Reconnecting...')
  time.sleep(10)
  machine.reset()

try:
  client = connect_and_subscribe()
except OSError as e:
  restart_and_reconnect()

while True:
  try:
    client.check_msg()
    if (time.time() - last_message) > message_interval:
      sensor.measure()
      temp = sensor.temperature()
      msg = b'MSG %d %3.1f' % (counter,temp) 
      client.publish(topic_pub, msg)
      last_message = time.time()
      counter += 1
  except OSError as e:
    restart_and_reconnect()





