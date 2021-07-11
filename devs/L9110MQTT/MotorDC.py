from machine import Pin,PWM
class MotorDC:
    kind = 'MotorDC'
    def __init__(self,pin_vel,pin_dir):
        self.Pwm = PWM(Pin(pin_vel), freq=1000 ,duty = 0)
        self.Dir= Pin(pin_dir, Pin.OUT)
   
    def velocidade(self, valor):
        self.Pwm.duty(valor)

    def sentido(self, sen = 0):
        if sen == 0:
            self.Dir.off()
        else:
            self.Dir.on()

