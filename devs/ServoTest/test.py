### Código para teste do servo motor 
# http://docs.micropython.org/en/v1.12/esp8266/tutorial/pwm.html
# A método duty define o valor de giro do servo.  
# - Varia de 1 a 127 para um mapeamento ruidoso de 0 graus a 180 para servos 180
# A função angle tenta tratar o ruído e gerar um valor mais confiável para 
# o controle do ângulo do eixo do servo 


import machine
import time, math

minDuty = 20
meanDuty = 65
maxDuty = 110 


def angle(degree):
    """ Converte de 10 a 170 graus para duty """  
    if degree >= 90:
        if degree <= 170:
            # nomaliza de [90, 170] para [0, 1]
            d = (degree - 90)/80 # 80 -> 170 - 90 
            duty = meanDuty + (d*(maxDuty - meanDuty))
        else:
            duty = maxDuty 
    else:
        if degree >= 10:
            # nomaliza de [10, 90] para [0, 1] 
            d = (degree - 10)/80 
            duty = minDuty + (d*(meanDuty - minDuty))
        else:
            duty = minDuty 
    return int(duty) 

servo = machine.PWM(machine.Pin(14), freq=50) #Determinar a frequência e controle por meio do PWM
for i in range(18):
    servo.duty(angle(i*10)) 
    time.sleep(1)
 