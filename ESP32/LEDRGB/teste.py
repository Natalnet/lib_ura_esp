# Complete project details at https://RandomNerdTutorials.com

import machine, neopixel

n = 1
p = 5

np = neopixel.NeoPixel(machine.Pin(p), n)

np[0] = (255, 150, 10)

np.write()