from machine import Pin,PWM

pinDVelocidade = 13
pinDDirecao = 12 

pwmD =  PWM(Pin(pinDVelocidade), freq=1000 ,duty = 0) 
direcaoD = Pin( pinDDirecao, Pin.OUT )

# ajusta a velocidade no sentido anti-horário 
pwmD.duty(0)
direcaoD.on()

# ajusta a velocidade no sentido horário 
pwmD.duty(1000)
direcaoD.off()

# diminui a veolocidade de rotação, em relação ao valor 1000 e dureção off 
pwmD.duty(700)

## Motor Esquerdo 
pinEVelocidade = 5
pinEDirecao = 23 

pwmE =  PWM(Pin(pinEVelocidade), freq=1000 ,duty = 0) 
direcaoE = Pin( pinEDirecao, Pin.OUT )


# ajusta a velocidade no sentido horário 
pwmE.duty(0)
direcaoE.on()

# ajusta a velocidade no sentido anti-horário 
pwmE.duty(1000)
direcaoE.off()

# diminui a veolocidade de rotação, em relação ao valor 1000 e direção off 
pwmE.duty(700)



