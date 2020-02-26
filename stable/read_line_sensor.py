from machine import  Pin

# GPIO 0 -> D8 https://alselectro.wordpress.com/2018/04/14/wifi-esp8266-development-board-wemos-d1/ 
pinL = machine.Pin(15, machine.Pin.IN,  machine.Pin.PULL_UP)

pinL.value()
