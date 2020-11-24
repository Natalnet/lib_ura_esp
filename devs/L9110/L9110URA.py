
## Motor A - Esquerdo  
# Sugestão de Pinos 
#A_IA  -->  Motor A PWM Speed
#A_IB  -->  Motor A Direction 

## Motor B - Direito 
# Sugestão de Pinos 
#B_IA  -->  Motor B PWM Speed --> 13
#B_IB  -->  Motor B Direction --> 12 



 

from MotorDC import MotorDC
class L9110URA(MotorDC): 
    def __init__ (self, pinVelL,pinDirL,pinVelD,pinDirD):
        self.name = 'L9110URA'
        self.motorEsquerdo = MotorDC(pinVelL,pinDirL)
        self.motorDireito = MotorDC(pinVelD,pinDirD)

    def frente(self, vel = 0):
        self.configura(0,vel,0,vel)

    def re(self):
        self.configura(1,1000,1,1000)
        
    def esquerda(self):
        self.configura(1,1000,0,0)
        
    def direita(self):
        self.configura(0,0,1,1000)
        
    def parar(self):
        self.configura(1,0,1,0)

    def configura(self, sA, vA, sB, vB):
        self.motorEsquerdo.sentido(sA)
        self.motorEsquerdo.velocidade(vA)
        self.motorDireito.sentido(sB)
        self.motorDireito.velocidade(vB)

