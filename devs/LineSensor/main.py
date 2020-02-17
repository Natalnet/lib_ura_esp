from machine import  Pin
# Pinos reservados para o sensor de linha 
pinEsq = 12 #D6 
pinDir = 14 #D5
sensorLinhaEsq = machine.Pin(pinEsq, machine.Pin.IN,  machine.Pin.PULL_UP)
sensorLinhaDir = machine.Pin(pinDir, machine.Pin.IN, machine.Pin.PULL_UP)


import time 
from rodas import Rodas 
r = Rodas()

parar =  False 

delta = 40 

## O sensor retorna 1 para branco e 0 para preto 
while ( not parar ):
  time.sleep_ms(delta) 
  if ( sensorLinhaDir.value() and sensorLinhaEsq.value() ): 
    r.frente()
  elif ( not sensorLinhaDir.value() and not sensorLinhaEsq.value() ):
    r.parar()
    parar = True
  elif ( not sensorLinhaEsq.value() ):
    r.esquerda()
  elif ( not  sensorLinhaDir.value() ):
    r.direita() 

 


