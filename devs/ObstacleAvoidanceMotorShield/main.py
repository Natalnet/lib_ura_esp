from hcsr04 import HCSR04
import utime

sensor = HCSR04(trigger_pin=14, echo_pin=12)

while True:
    distance = sensor.distance_cm()
    if distance<40:
        #print('Vire para Esquerda')
        r.esquerda()
        utime.sleep_ms(50)
    else:
        #print('Siga em Frente')
        r.frente()
    #print('Distance:', distance, 'cm')
    utime.sleep_ms(50)
