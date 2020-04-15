from machine import Pin,PWM
#A_IA  -->  Motor A PWM Speed
#A_IB  -->  Motor A Direction 
class DCMotor:
    kind = 'DCMotor'
    def __init__(self,pinSpeed,pinDir):
        self.Pwm = PWM(Pin(pinSpeed), freq=1000 ,duty = 0)
        self.Dir= Pin(pinDir, Pin.OUT)
   
    def speed(self, v):
        self.Pwm.duty(v)

    def direction(self, s = 0):
        if s == 1:
            self.Dir.off()
        else:
            self.Dir.on()

