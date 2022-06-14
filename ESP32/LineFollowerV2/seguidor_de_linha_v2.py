import machine
# Pinos reservados para o sensor de linha 
pinEsq = 14
pinDir = 27 
sensorLinhaEsq = machine.Pin(pinEsq, machine.Pin.IN, machine.Pin.PULL_UP)
sensorLinhaDir = machine.Pin(pinDir, machine.Pin.IN, machine.Pin.PULL_UP)


from L9110URA import L9110URA 
import time 

robo = L9110URA(13,12,5,23)

# Comportamentos 
from Comportamento import Comportamento
## Seguidor de linha 
comportamento = Comportamento(robo,sensorLinhaEsq,sensorLinhaDir)

cont = 0 
while cont < 30:
  respostaTerminal = comportamento.seguirLinha()
  print(respostaTerminal) 
  cont = cont + 1 

