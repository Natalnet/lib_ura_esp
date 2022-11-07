# Contador de cliques 
import machine
import time
button = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_UP)
count = 0
clicked = False 
countClicks = 0 
before = button.value()
while count < 10000:
  time.sleep(0.001)
  current = button.value()
  if before and not current:
    clicked = True 

  if clicked: 
    time.sleep(0.01)
    print('Button pressed!')
    countClicks = countClicks + 1 
    print('Clicks: ',countClicks)
    clicked = False 
  count = count + 1
  before = current 

