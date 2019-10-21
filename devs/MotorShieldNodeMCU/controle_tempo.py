
#from rodas import Rodas

import time 


class ControleTempo: 
  ## Permite executar um comando do robo durante um 
  ## intervalo predeterminado de tempo 
  def __init__ (self):
    print("Controle Tempo2: ") 
    # intervalo padrao de execucao do tempo 
    self.delta = 3500
    # guarda o inicio da execucao do comando 
    self.tempoInicial = 0
    # idica quando o proximo comando esta liberado para execucao 
    self.proximo = True 
    # marca a execucao de um comando 
    self.emExecucao = False 
  
  def aceitarProximoComando(self):
    if self.emExecucao:
      return False
    else:
      self.proximo = True
      return True   
    
  def escolheComando(self, cmd):
    if (cmd == 'f'):
      print("frente") 
    elif (cmd == 'r'): 
      print("re")
    elif (cmd == 'd'):
      print("direita")
    elif (cmd == 'e'): 
      print("esquerda") 
      
  def executaComando(self, cmd):
    execucao = False 
    if self.proximo:
      if self.emExecucao: 
        tempoAtual = time.ticks_ms()
        if tempoAtual - self.tempoInicial > self.delta and self.proximo  : 
          self.emExecucao = False
          self.proximo = False 
      else:
        self.tempoInicial = time.ticks_ms() 
        self.escolheComando(cmd)
        self.emExecucao = True
        execucao = True 
    return execucao  
