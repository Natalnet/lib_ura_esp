from machine import  Pin
# Pinos reservados para o sensor de linha 
pinEsq = 12 #D6 
pinDir = 14 #D5
sensorLinhaEsq = Pin(pinEsq, Pin.IN, Pin.PULL_UP)
sensorLinhaDir = Pin(pinDir, Pin.IN, Pin.PULL_UP)


import time 

parar =  False 

delta = 1000 

## O sensor retorna 1 para branco e 0 para preto 
while ( not parar ):
  time.sleep_ms(delta) 
  if ( sensorLinhaDir.value() and sensorLinhaEsq.value() ): 
    print("Siga em frente!") 
  elif ( not sensorLinhaEsq.value() ):
    print("Gira par esquerda!")
  elif ( not  sensorLinhaDir.value() ): 
    print("Gira para direita!") 
  if ( not sensorLinhaDir.value() and not sensorLinhaEsq.value() ):
    print("Para")
    parar = True
 


