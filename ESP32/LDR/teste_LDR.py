# Teste com o LED embutido na placa NodeMCU ESP32 
#Fonte:  https://RandomNerdTutorials.com
  

from machine import Pin, ADC

ldr = ADC(Pin(33))

ldr.atten(ADC.ATTN_11DB)       #Full range: 3.3v 

ldr_value = ldr.read()
print(ldr_value)
