

from MotorDC import MotorDC 
## Direito 
m1 = MotorDC(13,12)
## Esquerdo 
m2 = MotorDC(5,23)
import time 

# Motor 1 girando no sentido anti-horário - Direito
m1.velocidade(0)
m1.sentido(1)
time.sleep(1)

# Motor 1 girando no sentido horário 
m1.velocidade(1000)
m1.sentido(0)
time.sleep(1)

# Motor 1 parado 
m1.velocidade(0)
m1.sentido(0)
time.sleep(1) 

# Motor 2 girando no sentido horário - Esquerdo
m2.velocidade(0)
m2.sentido(1)
time.sleep(1)

# Motor 2 girando no sentido anti-horário 
m2.velocidade(1000)
m2.sentido(0)
time.sleep(1)

# Motor 2 parado 
m2.velocidade(0)
m2.sentido(0)
