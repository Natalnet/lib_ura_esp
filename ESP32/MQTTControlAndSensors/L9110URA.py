
## Motor A - Esquerdo  
# Sugestão de Pinos 
#A_IA  -->  Motor A PWM Speed --> 13 
#A_IB  -->  Motor A Direction --> 12 

## Motor B - Direito 
# Sugestão de Pinos 
#B_IA  -->  Motor B PWM Speed --> 5
#B_IB  -->  Motor B Direction --> 23 

from MotorDC import MotorDC
import time 
class L9110URA(MotorDC): 
    def __init__ (self, pinVelE,pinDirE,pinVelD,pinDirD):
        self.name = 'L9110URA'
        self.motorEsquerdo = MotorDC(pinVelE,pinDirE)
        self.motorDireito = MotorDC(pinVelD,pinDirD)
        self.configura(0,0,0,0) # parar

    # 0 velocidade mínima e 1000 velocidade máxima 
    def frente(self, vel = 1000):
        self.configura(1,1000 - vel,1,1000 - vel)

    # 0 velocidade mínima e 1000 velocidade máxima 
    def re(self, vel = 1000):
        self.configura(0,vel,0,vel)
        
    def esquerda(self):
        self.configura(0,1000,1,0)
        
    def direita(self):
        self.configura(1,0,0,1000)
        
    def parar(self):
        self.configura(0,0,0,0)

    def configura(self, sA, vA, sB, vB):
        self.motorEsquerdo.sentido(sA)
        self.motorEsquerdo.velocidade(vA)
        self.motorDireito.sentido(sB)
        self.motorDireito.velocidade(vB)

    def passoFrente(self):
        self.configura(1,0,1,0)
        time.sleep_ms(300)
        self.configura(0,0,0,0) # parar
    
    def passoRe(self):
        self.configura(0,1000,0,1000)
        time.sleep_ms(300)
        self.configura(0,0,0,0) # parar

    def passoEsquerda(self):
        self.configura(0,1000,1,0) 
        time.sleep_ms(150)
        self.configura(0,0,0,0) # parar

    def passoDireita(self):
        self.configura(1,0,0,1000) 
        time.sleep_ms(150)
        self.configura(0,0,0,0) # parar

