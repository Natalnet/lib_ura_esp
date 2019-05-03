import machine

p12 = machine.Pin(12) #Definindo o pino que irá ser utilizado 
pwm12 = machine.PWM(p12) #Define como PWM   
pwm12.freq(1) 
pwm12.duty(512)
