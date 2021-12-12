import time
counter = 0 
message_interval = 1
last_message = 0


while counter < 10:
  try:
 
    if (time.time() - last_message) > message_interval:
      counter += 1
      print(counter)
      
 
      last_message = time.time()
      
  except OSError as e:
    print(e) 




