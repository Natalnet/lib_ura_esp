# Complete project details at https://RandomNerdTutorials.com

import machine, neopixel

n = 1
p = 5

np = neopixel.NeoPixel(machine.Pin(p), n)

np[0] = (0, 0, 255)

np.write()