import Adafruit_BBIO.PWM as PWM
import time

servo_pin = "P8_19"
duty_min = 3
duty_max = 14.5
duty_span = duty_max - duty_min

PWM.start(servo_pin, (100-duty_min), 60.0, 1)
x= 15
angle = x

    
            
angle_f = float(angle)
duty = 100 - ((angle_f / 180) * duty_span + duty_min) 
PWM.set_duty_cycle(servo_pin, duty)
time.sleep(.1)
x = 90
time.sleep(5)
x = 180
time.sleep(2)
PWM.stop(servo_pin)
PWM.cleanup()
