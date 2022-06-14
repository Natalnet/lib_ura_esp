import time
from ControlState import ControlState
cs = ControlState() 
counter = 0 
message_interval = 1
last_message = 0
cs.executePrograma("FRT;FRT;ESQ;ESQ;FRT;FRT")

while counter < 20:
  try:
 
    if (time.time() - last_message) > message_interval:
      counter += 1
      print(counter)
      cs.updateExecution()
      cs.showState()
      last_message = time.time()
      
  except OSError as e:
    print(e) 




