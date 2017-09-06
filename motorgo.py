import time
import rcpy 
import rcpy.motor as motor
from rcpy.motor import motor3
from rcpy.motor import motor4



duty = .5

def Fmotor():
     motor4.set(duty)
     motor3.set(duty)
     
def Bmotor():
     motor4.set(-duty)
     motor3.set(-duty)

def Smotor():
     motor4.set(0)
     motor3.set(0)

Fmotor()
time.sleep(5)
Bmotor()
time.sleep(5)

     
