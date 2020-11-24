import time 

from MotorDC import MotorDC 
## Esquerdo 
m1 = MotorDC(13,12)
##  Right 
m2 = MotorDC(5,23)

# Motor 1 girando para um lado 
m1.velocidade(0)
m1.sentido(0)
time.sleep(1)

# Motor 1 girando para o um lado 
m1.velocidade(1000)
m1.sentido(1)
time.sleep(1)

# Motor 1 parado 
m1.velocidade(0)
m1.sentido(1)
time.sleep(1) 

# Motor 2 girando para um lado 
m2.velocidade(0)
m2.sentido(0)
time.sleep(1)

# Motor 2 girando para o um lado 
m2.velocidade(1000)
m2.sentido(1)
time.sleep(1)

# Motor 2 parado 
m2.velocidade(0)
m2.sentido(1)
