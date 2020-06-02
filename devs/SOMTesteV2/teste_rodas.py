from servo_motor import Servo


from rodas import Rodas

import time 

r = Rodas()


sf = Servo(14) 

r.frente()

time.sleep_ms(1000) 
sf.setAngle(170)
r.parar()

time.sleep_ms(1000) 
sf.setAngle(10)