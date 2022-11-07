# From: https://learn.adafruit.com/micropython-hardware-digital-i-slash-o/digital-inputs 
import machine
button = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_UP)
cont = 0
while cont < 2000:
  if not button.value():
    print('Button pressed!')
  else:
    print('Not pressed!')
  cont = cont + 1