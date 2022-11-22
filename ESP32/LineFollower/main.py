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
delta = 10 
## O sensor retorna 1 para linha preta e 0 para fundo claro 
while ( not parar ):
  time.sleep_ms(delta) 
  if ( not sensorLinhaDir.value() and not sensorLinhaEsq.value() ):
    dr.parar()
    time.sleep_ms(2) 
    dr.frente(900) 
  elif ( sensorLinhaDir.value() and  sensorLinhaEsq.value() ):
    dr.re()
    time.sleep_ms(50) 
  elif ( sensorLinhaEsq.value() ):
    dr.parar()
    time.sleep_ms(5) 
    dr.esquerda()
  elif ( sensorLinhaDir.value() ):
    dr.parar()
    time.sleep_ms(5) 
    dr.direita() 

