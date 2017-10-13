import Adafruit_BBIO.PWM as PWM
import time

PWM.start("P9_10", 50)
PWM.set_duty_cycle("P9_10", 100)

time.sleep(5)
PWM.stop("P9_10")
PWM.cleanup()