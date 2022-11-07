# From:  https://learn.adafruit.com/micropython-hardware-digital-i-slash-o/digital-inputs

import machine
import time
button = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_UP)
cont = 0
while cont < 1000:
  first = button.value()
  time.sleep(0.01)
  second = button.value()
  if first and not second:
    print('Button pressed!')
  elif not first and second:
    print('Button released!')
  cont = cont + 1
