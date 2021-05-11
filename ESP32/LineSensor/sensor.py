# Teste com o LED embutido na placa NodeMCU ESP32 

import machine
import time 

pinNum = 4 #D4 

sensor = machine.Pin(pinNum, machine.Pin.IN,  machine.Pin.PULL_UP)
n = 20 
delta = 500 
# Este código faz n leituras 
# O intervalo de cada leitura é delta milisegundos 
for c in range(n):
    print( sensor.value() )
    time.sleep_ms(delta) 
