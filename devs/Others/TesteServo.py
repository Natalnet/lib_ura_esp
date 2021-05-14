import machine
import time, math

servo = machine.PWM(machine.Pin(12), freq=50) #Determinar a frequência e controle por meio do PWM
for i in range(10):
    servo.duty(63) #Dar o valor de giro do servo.  Varia de  1 a 127 (0 graus a 180 para servos 180)
    time.sleep(1)
    servo.duty(1)
    time.sleep(1)
    servo.duty(127)
    time.sleep(1)
    servo.duty(2)


