from hcsr04 import HCSR04
import time

# GPIOs for NodeMCU ESP8266 D5 and D6 
sensor = HCSR04(trigger_pin=14, echo_pin=12)

while True:
    distance = sensor.distance_cm()
    print('Distance:', distance, 'cm')
    time.sleep(1)
