# Teste com a placa NodeMCU ESP32 
#Fonte:  https://RandomNerdTutorials.com
  

from machine import Pin, ADC
import time 

ldr = ADC(Pin(12))

ldr.atten(ADC.ATTN_11DB)        

for i in range(50):
    ldr_value = ldr.read()
    print(ldr_value)
    time.sleep_ms(300)

