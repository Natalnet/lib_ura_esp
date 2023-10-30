import machine
# Pinos reservados para o sensor de linha 
pinEsq = 18 
pinDir = 19 
sensorLinhaEsq = machine.Pin(pinEsq, machine.Pin.IN, machine.Pin.PULL_UP)
sensorLinhaDir = machine.Pin(pinDir, machine.Pin.IN, machine.Pin.PULL_UP)


from L9110URA import L9110URA 
import time 

dr = L9110URA(13,12,5,23) 

parar =  False 
 
deltaMove = 50
deltaStop = 30
## O sensor retorna 1 para linha preta e 0 para fundo claro 
while ( not parar ):
  time.sleep_ms(deltaMove)
  dr.parar()
  time.sleep_ms(deltaStop)
  if ( not sensorLinhaDir.value() and not sensorLinhaEsq.value() ):
    dr.frente(900) 
    #print('Frente!')
  elif ( sensorLinhaDir.value() and  sensorLinhaEsq.value() ):
    dr.re()
    #print('Re!')
  elif ( sensorLinhaEsq.value() ): 
    dr.esquerda()
    #print('Esquerda!')
  elif ( sensorLinhaDir.value() ):
    dr.direita() 
    #print('Direita!')

