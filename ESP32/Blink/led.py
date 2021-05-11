# Teste com o LED embutido na placa NodeMCU ESP32 

import machine

pin = machine.Pin(2, machine.Pin.OUT)

# Comandos para liga o LED azul  
pin.on()

pin.value(1) 

# Comandos para desliga o LED azul  
pin.off() 

pin.value(0) 