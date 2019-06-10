
#B_IA  -->  Motor B PWM Speed
#B_IB  -->  Motor B Direction 

from MotorDC import MotorDC
class L9110URA(MotorDC): 
    def __init__ (self, pinVelL,pinDirL,pinVelD,pinDirD):
        self.name = 'L9110URA'
        self.motorLeft = MotorDC(pinVelL,pinDirL)
        self.motorRight = MotorDC(pinVelD,pinDirD)

    def forward(self):
        self.motorLeft.s(1)
        self.motorLeft.v(1000)
        self.motorRight.s(1)
        self.motorRight.v(900) 

    def backward(self):
        self.motorLeft.s(0)
        self.motorLeft.v(0)
        self.motorRight.s(0)
        self.motorRight.v(100) 
        
    def turnLeft(self):
        self.motorLeft.s(0)
        self.motorLeft.v(0)
        self.motorRight.s(1)
        self.motorRight.v(1000)  
        
    def turnRight(self):
        self.motorLeft.s(1)
        self.motorLeft.v(1000)
        self.motorRight.s(0)
        self.motorRight.v(0) 
        
    def stop(self):
        self.motorLeft.s(1)
        self.motorLeft.v(0)
        self.motorRight.s(1)
        self.motorRight.v(0)


