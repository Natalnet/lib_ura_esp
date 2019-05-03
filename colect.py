from hcsr04 import HCSR04
import time, math, machine

"""
    Colect data for a ultrasonic sensor in 180 degrees
    Copyright (C) 2018  William Ribeiro (willcribeiro)

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program. If not, see <http://www.gnu.org/licenses/>.

    contact :   https://github.com/willcribeiro or
                 william-cribeiro@bct.ect.ufrn.br

    """


def coleta():

    sensor = HCSR04(trigger_pin=16, echo_pin=0)
    servo = machine.PWM(machine.Pin(12), freq=50)
    distance = sensor.distance_cm()

    i=30
    servo.duty(30)

    while i<115: #Giro do servo
    
        servo.duty(i)
        time.sleep(0.5)
        distance = sensor.distance_cm() #Leitura do sensor
        time.sleep(0.5)
        if distance>60:
            print('60,',end='')
        else:
            print(distance,',',end='')
        time.sleep(0.5)
        i = i + 14 #Logica de rotação em 30 gráus
    print(' ')
    print('---x-----x----')
    time.sleep(1)
    
     