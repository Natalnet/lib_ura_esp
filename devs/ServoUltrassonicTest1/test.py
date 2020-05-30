## Teste com três leituras 
# Faz o teste combinando ultrassom e servo motor para coletar três 
# leituras de distância 

from hcsr04 import HCSR04
from servo_motor import Servo
import time
 
sensorD = HCSR04(trigger_pin=12, echo_pin=13)

amostra = [0,0,0]

sf = Servo(14)

angles = [10,90,170]

contI = 0
for a in angles:
    sf.setAngle(a)
    time.sleep_ms(500)
    amostra[contI] = sensorD.distance_cm() 
    time.sleep_ms(10)
    contI += 1 

distance = sensorD.distance_cm()
print('Amostra:', amostra)