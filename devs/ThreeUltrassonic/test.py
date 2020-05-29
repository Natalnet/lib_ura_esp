from hcsr04 import HCSR04
import utime

sensorF = HCSR04(trigger_pin=14, echo_pin=12)
sensorL = HCSR04(trigger_pin=13, echo_pin=15)
#sensorR = HCSR04(trigger_pin=16, echo_pin=34)

distance = sensorF.distance_cm()
print('Front:', distance, 'cm')

distance = sensorL.distance_cm()
print('Left:', distance, 'cm')

#distance = sensorR.distance_cm()
#print('Right:', distance, 'cm')