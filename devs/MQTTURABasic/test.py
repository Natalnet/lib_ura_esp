
#B_IA  -->  Motor B PWM Spdr.forward()eed
#B_IB  -->  Motor B Direction 

## Left
# m1 = MotorDC(13,12)
##  Right 
# m2 = MotorDC(5,23)

import L9110URA

dr = L9110URA(13,12,5,23) 

dr.forward()

dr.backward() 

dr.stop() 

dr.trunLeft() 

dr.turnRight() 
