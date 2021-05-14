from motorShield import MotorShield
import time

rodas = MotorShield()

def frente():
    rodas.directionRobot(1, 1)
    rodas.vel(600,600)

def re():
    rodas.directionRobot(0, 0)
    rodas.vel(600,600)

def parar():
    rodas.directionRobot(1, 1)
    rodas.vel(0,0)

def esq():
    rodas.directionRobot(1, 0)
    rodas.vel(300,300)
    time.sleep(1)

def dir():
    rodas.directionRobot(0, 1)
    rodas.vel(300,300)
    time.sleep(1)
