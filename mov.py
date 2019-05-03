from hcsr04 import HCSR04
from motorShield import MotorShield
import time, math, machine

#Definitions
sensor = HCSR04(trigger_pin=16, echo_pin=0)
servo = machine.PWM(machine.Pin(12), freq=50)
distance = sensor.distance_cm()
rodas = MotorShield()
rodas.directionRobot(1, 0)
rodas.vel(900,900)

print('antes do while') #Debugs prints
i = 30 #Angle

while True:

    distance = sensor.distance_cm()
    time.sleep(0.5)
    print(distance)
    print('antes do if')
    if distance<5:
        rodas.vel(0,0)
        while i<136: 
            servo.duty(i)
            distance2 = sensor.distance_cm()
            print('distancia',distance2)
            time.sleep(1)
            print(i)
            i = i + 21 #Increment 30 degrees

    else:
        print('entrei')
        rodas.vel(900,900)
        i = 30 #Reset angle
        servo.duty(72) #Servo in 90 degrees
