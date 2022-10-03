# More details can be found in TechToTinker.blogspot.com 
# George Bantique | tech.to.tinker@gmail.com

from machine import Pin
from machine import PWM
from time import sleep_ms

buzzer = PWM(Pin(23, Pin.OUT))
buzzer.init(freq=0, duty=0)

# Ajusta a frequência
buzzer.freq(1047)

# Ajusta a intensidade do barulho
buzzer.duty(256)
sleep_ms(1000)

# Zera o barulho
buzzer.duty(0)
sleep_ms(1000)

# Inicializa o barulho com uma frequência
buzzer.init(freq=69, duty=8)
sleep_ms(1000)
buzzer.duty(0)

# Desativa o pwm e libera a porta
buzzer.deinit()





