import Adafruit_BBIO.GPIO as GPIO
import time
     
GPIO.setup("P8_13", GPIO.OUT)
    
GPIO.output("P8_13", GPIO.HIGH)
time.sleep(5)
GPIO.output("P8_13", GPIO.LOW)
GPIO.cleanup()