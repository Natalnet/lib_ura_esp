# Complete project details at https://RandomNerdTutorials.com

import machine, neopixel

n = 16
p = 5

np = neopixel.NeoPixel(machine.Pin(p), n)
for i in range(n):
    np[i] = (150, 150, 30)

np.write()