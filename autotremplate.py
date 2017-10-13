from bbpystepper import Stepper
import Adafruit_BBIO.PWM as PWM
import Adafruit_BBIO.GPIO as GPIO
import time

servo = "P8_19"
duty_min = 3
duty_max = 14.5
duty_span = duty_max - duty_min
stp = Stepper()
stp.steps_per_rev = 4076
GPIO.setup("P8_10", GPIO.OUT)
PWM.start(servo, (100-duty_min), 60.0, 1)
 
while 1:
     answer = raw_input("what would you like to do:")
     
     if answer =='park':
         stp.rotate(360,10)
         PWM.set_duty_cycle(servo,93.806)
         GPIO.output("P8_10", GPIO.HIGH)
         time.sleep(1)
         GPIO.output("P8_10", GPIO.LOW)
     elif answer == 'stop':
         print "ok"
         PWM.stop(servo)
         PWM.cleanup()
         GPIO.output("P8_10", GPIO.LOW)
         GPIO.cleanup()
         break
        
     
         