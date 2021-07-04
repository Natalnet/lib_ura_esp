from hcsr04 import HCSR04
 
sensor = HCSR04(trigger_pin=19, echo_pin=18)

distance = sensor.distance_cm()

print('Distance:', distance, 'cm')
 
