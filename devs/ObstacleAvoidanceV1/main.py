from hcsr04 import HCSR04
import utime

sensor = HCSR04(trigger_pin=16, echo_pin=0)

while True:
    distance = sensor.distance_cm()
    if distance<30:
        print('Vire para Direita')
        dr.turnLeft()
    else:
        print('Siga em Frente')
        dr.forward()
    print('Distance:', distance, 'cm')
    utime.sleep_ms(1000)
