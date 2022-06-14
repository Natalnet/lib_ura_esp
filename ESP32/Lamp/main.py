# Complete project details at https://RandomNerdTutorials.com

def sub_cb(topic, msg):
  global topic_sub
  global lamp_staus
  print((topic, msg))
  print(topic_sub)
  if topic == topic_sub and msg == b'ON':
    print('ESP received, turn on the lamp')
    lamp.on() 
    lamp_staus = 'ON'
  if topic == topic_sub and msg == b'OFF':
    print('ESP received, turn off the lamp')
    lamp.off()
    lamp_staus = 'OFF'

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
      msg = b'%s %d' % (lamp_staus,counter)
      client.publish(topic_pub, msg)
      last_message = time.time()
      counter += message_interval
  except OSError as e:
    restart_and_reconnect()




