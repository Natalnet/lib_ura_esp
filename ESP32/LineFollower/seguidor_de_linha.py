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
delta = 1000 
## O sensor retorna 1 para branco e 0 para preto 
while ( not parar ):
  time.sleep_ms(delta) 
  if ( sensorLinhaDir.value() and sensorLinhaEsq.value() ): 
    dr.frente()
  elif ( not sensorLinhaDir.value() and not sensorLinhaEsq.value() ):
    dr.parar()
    parar = True
  elif ( not sensorLinhaEsq.value() ):
    dr.esquerda()
  elif ( not  sensorLinhaDir.value() ):
    dr.direita() 

 


