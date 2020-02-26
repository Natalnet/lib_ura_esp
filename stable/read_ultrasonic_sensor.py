from hcsr04 import HCSR04

# for wemos D8 -> 0 e D7 -> 16 
sensor = HCSR04(trigger_pin=16, echo_pin=0)

distance = sensor.distance_cm()

print('Distance:', distance, 'cm')
