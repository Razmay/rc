import Adafruit_BBIO.PWM as PWM
import time

servo_pin = "P8_19"
duty_min = 3
duty_max = 14.5
duty_span = duty_max - duty_min

PWM.start(servo_pin, (100-duty_min), 60.0, 1)
PWM.set_duty_cycle(servo_pin, 91.25)
