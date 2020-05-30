import machine



class Servo: 
    servoMotor = 0 

    minDuty = 20
    meanDuty = 65
    maxDuty = 110 

    def __init__(self, sPin):
        self.servoMotor = machine.PWM(machine.Pin(sPin), freq=50)

    def conf(self,mi,me,ma):
        self.minDuty = mi
        self.meanDuty = me 
        self.maxDuty = ma 

    # http://docs.micropython.org/en/v1.12/esp8266/tutorial/pwm.html
    # A método duty define o valor de giro do servo.  
    # - Varia de 1 a 127 para um mapeamento ruidoso de 0 graus a 180 para servos 180
    # A função angle tenta tratar o ruído e gerar um valor mais confiável para 
    # o controle do ângulo do eixo do servo 
    def angle(self, degree):
        """ Converte de 10 a 170 graus para duty """  
        duty = self.minDuty 
        if degree >= 90:
            if degree <= 170:
                # nomaliza de [90, 170] para [0, 1]
                d = (degree - 90)/80 # 80 -> 170 - 90 
                duty = self.meanDuty + (d*(self.maxDuty - self.meanDuty))
            else:
                duty = self.maxDuty 
        else:
            if degree >= 10:
                # nomaliza de [10, 90] para [0, 1] 
                d = (degree - 10)/80 
                duty = self.minDuty + (d*(self.meanDuty - self.minDuty))
            else:
                duty = self.minDuty 
        return int(duty) 

    def setAngle(self, degree):
        self.servoMotor.duty(self.angle(degree)) 
     