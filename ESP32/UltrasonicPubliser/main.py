# Complete project details at https://RandomNerdTutorials.com
 
def client_connect():
  global client_id, mqtt_server, topic_sub, server_port, mqtt_user, mqtt_password
  client = MQTTClient(client_id, mqtt_server, server_port, mqtt_user, mqtt_password)
  client.connect()
  print('Connected to %s MQTT broker!' % (mqtt_server))
  return client

def restart_and_reconnect():
  print('Failed to connect to MQTT broker. Reconnecting...')
  time.sleep(10)
  machine.reset()

try:
  client = client_connect()
except OSError as e:
  restart_and_reconnect()

while True:
  try:
    if (time.time() - last_message) > message_interval:
      # write on output topic  
      distance = sensor.distance_cm()
      #msg = b'Distance: %d cm' % distance 
      msg = b'%d' % distance 
      client.publish(topic_pub, msg)
      last_message = time.time()
      counter += message_interval    
  except OSError as e:
    restart_and_reconnect()




