
#B_IA  -->  Motor B PWM Speed
#B_IB  -->  Motor B Direction 

# from dcmotor import DCMotor
## Left for D1 Wemos 
# m1 = DCMotor(13,12) 
##  Right  
# m2 = DCMotor(14,4)

from L9110URA import L9110URA

dr = L9110URA(13,12,14,4) 

dr.forward()

dr.backward() 

dr.stop() 

dr.turnLeft() 

dr.turnRight() 
