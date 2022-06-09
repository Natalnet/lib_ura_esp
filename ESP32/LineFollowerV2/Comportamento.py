import time 
FRENTE = 1 
DIREITA = 2 
ESQUERDA = 3 
RE = 4 

class Comportamento:
    kind = 'Comportamento'
    def __init__ (self, _motores, _sensorLinhaEsq, _sensorLinhaDir):
        self.rodas = _motores
        self.sensorLinhaEsq = _sensorLinhaEsq
        self.sensorLinhaDir = _sensorLinhaDir 
        self.tempoAcao = 200
        self.potenciaMaxima = 800
        self.potenciaLimiar = 500
        self.deltaMov = 15
        self.deltaGiro = 5
        self.movEsquerda = 0 
        self.movDireita = 0
        self.quantidadeNiveis = 5
        self.deltaPotencia = int( (self.potenciaMaxima - self.potenciaLimiar) / self.quantidadeNiveis )
        self.estadoAtual = 0
        self.estadoAnterior = -1 
        self.nivelPotencia = 0
        self.tempoPausa = 1000

    def obtenPotenciaPorNivel(self):
        return self.potenciaLimiar + self.deltaPotencia * self.nivelPotencia

    def incrementaNivelPotencia(self):
        self.nivelPotencia = self.nivelPotencia + 1 
        if self.nivelPotencia > self.quantidadeNiveis: 
            self.nivelPotencia =  self.quantidadeNiveis

    def seguirLinha(self): 
        msg = ''


        valorSLE = self.sensorLinhaEsq.value()
        valorSLD = self.sensorLinhaDir.value()
        #print("E: ", valorSLE, " D: ", valorSLD)  
        
        if ( not valorSLD and not valorSLE ): 
            self.estadoAnterior = self.estadoAtual
            self.estadoAtual = FRENTE
        elif (  valorSLD and  valorSLE ):
            self.estadoAnterior = self.estadoAtual
            self.estadoAtual = RE
        elif ( valorSLD ):
            self.estadoAnterior = self.estadoAtual
            self.estadoAtual = DIREITA
        elif ( valorSLE ):
            self.estadoAnterior = self.estadoAtual
            self.estadoAtual = ESQUERDA 
        semTrocaDeEstado = False  
        if (self.estadoAnterior == self.estadoAtual ): 
            semTrocaDeEstado = True 

        if self.estadoAtual == FRENTE and semTrocaDeEstado: 
            self.rodas.motores(self.movEsquerda,self.movDireita)
            msg = '%s %d %d' % ("Frente!",self.movEsquerda,self.movDireita)
        elif self.estadoAtual == RE and semTrocaDeEstado: 
            self.rodas.motores(self.movEsquerda,self.movDireita)
            msg =  '%s %d %d' % ("Re!",-self.movEsquerda,-self.movDireita)
        elif self.estadoAtual == DIREITA and semTrocaDeEstado: 
            self.rodas.motores(self.movEsquerda,-self.movDireita)
            msg =  '%s %d %d' % ("Direito!",self.movEsquerda, - self.movDireita)
        elif self.estadoAtual == ESQUERDA and semTrocaDeEstado: 
            self.rodas.motores(-self.movEsquerda,self.movDireita)
            msg =  '%s %d %d' % ("Esquerdo!",-self.movEsquerda,self.movDireita)        


        if self.estadoAtual == self.estadoAnterior:
            self.incrementaNivelPotencia()
                 
            time.sleep_ms(self.tempoAcao)
        else: 
            self.nivelPotencia = 0
            self.rodas.parar() 
            msg = "Parar!"
            time.sleep_ms(self.tempoPausa)  
        self.movEsquerda = self.obtenPotenciaPorNivel() 
        self.movDireita = self.obtenPotenciaPorNivel()              
                     
        return msg 
            
