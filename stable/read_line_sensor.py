from machine import  Pin

# GPIO 0 -> D8 
pinL = machine.Pin(0, machine.Pin.IN,  machine.Pin.PULL_UP)

pinL.value()
