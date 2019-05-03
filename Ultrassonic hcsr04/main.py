from hcsr04 import HCSR04
import time

sensor = HCSR04(trigger_pin=16, echo_pin=0)

while True:
    distance = sensor.distance_cm()
    if distance<5:
        print('Menor que 5')
    else:
        print('Maior que 5')

    print('Distance:', distance, 'cm')
    time.sleep(1)
