

# -*- coding: utf-8 -*-

"""
    This module implements .
    :copyright: © 2018 by the Lindos team.
    :license: BSD, see LICENSE for more details.
"""

from motorx import MotorX

class MotorShield(MotorX):
    
    def __init__(self):
    
        """
            initializing the MotorShield class by instantiating MotorX class:
            
            instantiating to MotorA and MotorB 
            parameters from MotorX class who defines 
            a Pin to implement velocity and another Pin to 
            implement direction one for each motor:
            MotorX(nome, pin_vel, pin_direction);
            attributes:
            pin_vel: pin that it's responsible for attribute 
            a given velocity to the robot;
            pin_direction: pin that it's responsible for
            attribute a given direction (0 or 1) to the robot;
        """

        self.motorA = MotorX('motorA',5,0)
        self.motorB = MotorX('motorB',4,2)


    def vel(self,valueA, valueB):
        """
            defining vel method:
            it sets the velocity of MotorA and MotorB
            attributes:
            valueA: a velocity of 0 to 1023 for the MotorA;
            valueB: a velocity of 0 to 1023 for the MotorB;
        """
        try:
            self.motorA.speed(valueA)
            self.motorB.speed(valueB)
        except:
            print  ('carai em vel')    
    def stop(self):

        """
        
            definig stop method:
            it set velocity of both Motor (A and B) to 0;
        
            attributes:
            none;
        """

        self.vel(0, 0)

    def directionRobot(self, valueA = 0, valueB = 0, flag_invertAB= [0,0]):
     
        """
            defining the direction Robot method:
            it makes possible to define the direction of the 
            robot's motors; if not attributed, it defines as 0;
            attributes:
            valueA: a direction, 0 or 1, that defines if the robot 
            motorA goes front or backwards;
            valueB: a direction, 0 or 1, that defines if the robot
            motorB goes front or backwards;
        """
        if flag_invertAB==[0,1]:
            self.motorA.direction(valueA)
            self.motorB.direction(not valueB)
        elif flag_invertAB==[1,1]:
            self.motorA.direction(not valueA)
            self.motorB.direction(valueB)   
        elif flag_invertAB==[1,0]:
            self.motorA.direction( not valueA)
            self.motorB.direction( valueB)      
        else:
            self.motorA.direction(valueA)
            self.motorB.direction(valueB)
    
    def spin(self,value):

        """
            defining the spin method:
            it makes the robot spin by attributing a value to 
            motorA and given the motorB the "not value", putting the robot
            to spin for the side that you attribute the value;
            attributes:
            value: attribute a value to MotorA;
            
        """
        
        self.motorA.direction(value)
        self.motorB.direction((not value))
