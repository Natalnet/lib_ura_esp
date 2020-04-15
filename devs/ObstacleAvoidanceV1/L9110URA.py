
#B_IA  -->  Motor B PWM Speed
#B_IB  -->  Motor B Direction 

from dcmotor import DCMotor
class L9110URA(DCMotor): 
    def __init__ (self, pinVelL,pinDirL,pinVelD,pinDirD):
        self.name = 'L9110URA'
        self.motorLeft = DCMotor(pinVelL,pinDirL)
        self.motorRight = DCMotor(pinVelD,pinDirD)

    def forward(self):
        self.motorLeft.direction(1)
        self.motorLeft.speed(1000)
        self.motorRight.direction(1)
        self.motorRight.speed(1000) 

    def backward(self):
        self.motorLeft.direction(0)
        self.motorLeft.speed(0)
        self.motorRight.direction(0)
        self.motorRight.speed(0) 
        
    def turnLeft(self):
        self.motorLeft.direction(0)
        self.motorLeft.speed(0)
        self.motorRight.direction(1)
        self.motorRight.speed(1000)  
        
    def turnRight(self):
        self.motorLeft.direction(1)
        self.motorLeft.speed(1000)
        self.motorRight.direction(0)
        self.motorRight.speed(0) 
        
    def stop(self):
        self.motorLeft.direction(1)
        self.motorLeft.speed(0)
        self.motorRight.direction(1)
        self.motorRight.speed(0)

