
from motor import Motor
class MotorX(Motor):
    name = ''
    def __init__ (self, nome,pin_vel,pin_dir):
        self.name = nome
        Motor.__init__(self,pin_vel,pin_dir)

    def direction(self, val = 0):
        self.s(val)
        print( 'sentido motor', self.name, val)

    def speed(self , value):
        self.v(value)
        print ("speed motor" , self.name, value)