from hcsr04 import HCSR04
import utime

sensorF = HCSR04(trigger_pin=16, echo_pin=0)

distance = sensorF.distance_cm()

print('Front:', distance, 'cm')