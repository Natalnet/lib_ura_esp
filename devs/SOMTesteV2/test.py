from som import SOM 
from hcsr04 import HCSR04
from servo_motor import Servo
from rodas import Rodas
import time 

rodas = Rodas() 

sf = Servo(14)
som = SOM() 
sensorD = HCSR04(trigger_pin=12, echo_pin=13)


amostra = [0,0,0]

# Ângulos de posições: direita, frontal e esquerda 
angles = [10,90,170]

for i in range(10): 
    contI = 2
    for a in angles:
        sf.setAngle(a)
        time.sleep_ms(500)
        d = sensorD.distance_cm() 
        if d > 70: 
            d = 70
        amostra[contI] = d 
        time.sleep_ms(10)
        contI -= 1 
    print('Amostra:', amostra)
    acao = som.melhorReposta(amostra)
    print(acao) 

    # Escolhe executa a ação 
    if acao == 'f':
        rodas.frente()
    elif acao == 'e':
        rodas.esquerda()
    elif acao == 'd':
        rodas.direita()
    elif acao == 'r':
        rodas.re()

    amostra = [0,0,0]
    sf.setAngle(10)
    time.sleep_ms(1000)
    rodas.parar() 
    