from machine import  Pin
# Pinos reservados para o sensor de linha 
pinEsq = 12 #D6 
pinDir = 14 #D5
sensorLinhaEsq = Pin(pinEsq, Pin.IN, Pin.PULL_UP)
sensorLinhaDir = Pin(pinDir, Pin.IN, Pin.PULL_UP)

import time 
from rodas import Rodas 
r = Rodas()

delta = 40 
## O sensor retorna 1 para branco e 0 para preto 
while ( True ):
  r.parar()
  time.sleep_ms(delta) 
  if ( not sensorLinhaDir.value() and not sensorLinhaEsq.value() ): 
    r.frente()
  elif ( sensorLinhaEsq.value() ):
    r.esquerda()
  elif ( sensorLinhaDir.value() ):
    r.direita() 
  time.sleep_ms(delta) 

 


