# Complete project details at https://RandomNerdTutorials.com
def sub_cb(topic, msg):
  global topic_sub
  print((topic, msg))


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
  except OSError as e:
    restart_and_reconnect()




