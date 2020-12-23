# Complete project details at https://RandomNerdTutorials.com



def sub_cb(topic, msg):
  print((topic, msg))
  if topic == b'URA/robo1/acao' and msg == b'f':
    print('ESP received, forward')
    robot.forward() 
  if topic == b'URA/robo1/acao' and msg == b's':
    print('ESP received, stop')
    robot.stop()  
  if topic == b'URA/robo1/acao' and msg == b'l':
    print('ESP received,  turn left')
    robot.turnLeft()
    time.sleep_ms(commandTime)
    robot.stop()
  if topic == b'URA/robo1/acao' and msg == b'r':
    print('ESP received, turn right')
    robot.turnRight()  
    time.sleep_ms(commandTime)
    robot.stop()
  if topic == b'URA/robo1/acao' and msg == b'b':
    print('ESP received, backward')
    robot.backward()  
  command = msg; 
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
      # write on 'Hello' topic 
      msg = b'Oi #%d' % counter
      client.publish(topic_pub, msg)
      last_message = time.time()
      counter += 1
      # se o comando for par direita ou para esquerda o robo deve para depois de 300 ms 
    #currentCommandTime = time.ticks_ms(); 
    #if  (currentCommandTime - commandLastTime) > commandTime: 
    #  if command == b'l' or command == b'r':
    #    commandLastTime = currentCommandTime; 
    #    command = b'x'
    #    robot.stop()
    #    print('---') 
    #    print(command)
  except OSError as e:
    restart_and_reconnect()




