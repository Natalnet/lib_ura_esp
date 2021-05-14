from machine import Pin,PWM
class Motor:
    kind = 'motorDC'
    def __init__(self,pin_vel,pin_dir):
        self.Pwm = PWM(Pin(pin_vel), freq=1000 ,duty = 0)
        self.Dir= Pin(pin_dir, Pin.OUT)
   
    def v(self, value):
        self.Pwm.duty(value)

    def s(self, sentido = 0):
        if sentido == 1:
            self.Dir.off()
        else:
            self.Dir.on()