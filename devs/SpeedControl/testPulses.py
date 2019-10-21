from machine import Pin, ADC
from time import sleep

pot = ADC(Pin(36))
pot.atten(ADC.ATTN_11DB)       #Full range: 3.3v

cont = 0
while cont < 100:
  pot_value = pot.read()
  print(pot_value)
  sleep(0.1)
  cont=cont+1
 
