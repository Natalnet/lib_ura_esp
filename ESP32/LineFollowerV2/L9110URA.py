
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
        self.parametro1 = 0 
        self.parametro2 = 0 
        self.velocidadeReferenciaDir = 1000 
        self.velocidadeReferenciaEsq = 1000 
        self.cmdTempoMaximo = 5000 # tempo máximo que um comando deve ficar em execução 
        self.motorEsquerdo = MotorDC(pinVelE,pinDirE)
        self.motorDireito = MotorDC(pinVelD,pinDirD)
        self.configura(0,0,0,0) # parar

    def setVelocidades(self, _ve, _vd):
        self.velocidadeReferenciaDir = _ve 
        self.velocidadeReferenciaEsq = _vd  

    # ajuste de velocidade positiva ou negativa (ré) dos motores
    def motores(self, velEsq, velDir):
        direcaoDir = 1
        direcaoEsq = 1
        velocidadeEsq = self.velocidadeReferenciaEsq - velEsq 
        velocidadeDir = self.velocidadeReferenciaDir - velDir 
        if ( velEsq <= 0 ):
            direcaoDir = 0
            velocidadeEsq = -velEsq
        if ( velDir <= 0):
            direcaoEsq = 0 
            velocidadeDir = -velDir
        self.configura(direcaoDir,velocidadeEsq,direcaoEsq,velocidadeDir)

    # 0 velocidade mínima e 1000 velocidade máxima 
    def frente(self, vel = 1000):
        if vel > 1000:
            vel = 1000 
        self.configura(1,1000 - vel,1,1000 - vel)
        #print("Frente (",vel,")")

    # 0 velocidade mínima e 1000 velocidade máxima 
    def re(self, vel = 1000):
        self.configura(0,vel,0,vel)
        
    def esquerda(self):
        self.configura(0,self.velocidadeReferenciaEsq,1,0)
        
    def direita(self):
        self.configura(1,0,0,self.velocidadeReferenciaDir)
        
    def parar(self):
        self.configura(0,0,0,0)

    def configura(self, sA, vA, sB, vB):
        self.motorEsquerdo.sentido(sA)
        self.motorEsquerdo.velocidade(vA)
        self.motorDireito.sentido(sB)
        self.motorDireito.velocidade(vB)

    # Faz o robô entrar em modo sleep durante um tempo e depois envia o comando de parar os motores 
    def contaTempo(self, _t):        
        if ( _t > self.cmdTempoMaximo ):
            time.sleep_ms(self.cmdTempoMaximo)
        else:      
            time.sleep_ms(_t)
        self.configura(0,0,0,0) # parar

    def passoFrente(self, tempo = 300):
        self.configura(1,0,1,0)
        self.contaTempo(tempo) 
    
    def passoRe(self, tempo = 300):
        self.configura(0,self.velocidadeReferenciaEsq,0,self.velocidadeReferenciaDir)
        self.contaTempo(tempo) 

    def passoEsquerda(self, tempo = 150):
        self.configura(0,self.velocidadeReferenciaEsq,1,0) 
        self.contaTempo(tempo) 

    def passoDireita(self, tempo = 150):
        self.configura(1,0,0,self.velocidadeReferenciaDir) 
        self.contaTempo(tempo) 

    def executaComando(self, cmd):
        if cmd == 'FRT' or cmd == 'FTT':
            self.configura(1,1000-self.velocidadeReferenciaEsq,1,1000-self.velocidadeReferenciaDir)
            #print(cmd) 
        elif cmd == 'TRS' or cmd == 'TRT':
            self.configura(0,self.velocidadeReferenciaEsq,0,self.velocidadeReferenciaDir)
        elif cmd == 'DIR' or cmd == 'DRT':
            self.configura(1,0,0,self.velocidadeReferenciaDir)
        elif cmd == 'ESQ' or cmd == 'EST':
            self.configura(0,self.velocidadeReferenciaEsq,1,0) 
        elif cmd == 'PAR':
            self.configura(0,0,0,0)

