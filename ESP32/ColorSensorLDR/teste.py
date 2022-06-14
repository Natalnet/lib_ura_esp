# Fonte: https://RandomNerdTutorials.com

import neopixel
from machine import Pin, ADC
import time 

# LDR 
ldr = ADC(Pin(33))
ldr.atten(ADC.ATTN_11DB)  

n = 1
p = 5

# LED_RGB 
np = neopixel.NeoPixel(Pin(p), n)

# Defini a cor 
#np[0] = (0, 0, 255) # Blue 
np[0] = (255, 0, 0) # Red 
np.write()

# Espera um pouco e depois lê 
time.sleep_ms(1)
ldr_value = ldr.read()
time.sleep_ms(1)

# mostra o valor lido 
print(ldr_value)

np[0] = (0, 0, 255) # Blue 
np.write()


