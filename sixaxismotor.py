import Adafruit_BBIO.PWM as PWM
from triangula.input import SixAxis, SixAxisResource
import time 
with SixAxisResource() as joystick:
    
 servo_pin = "P8_19"
 duty_min = 3
 duty_max = 14.5
 duty_span = duty_max - duty_min

PWM.start(servo_pin, (100-duty_min), 60.0, 1)
# Button handler, will be bound to the square button later
def handler(button):
  print 'Button {} pressed'.format(button)

# Get a joystick, this will fail unless the SixAxis controller is paired and active
# The bind_defaults argument specifies that we should bind actions to the SELECT and START buttons to
# centre the controller and reset the calibration respectively.
with SixAxisResource(bind_defaults=True) as joystick:
    # Register a button handler for the square button
    joystick.register_button_handler(handler, SixAxis.BUTTON_SQUARE)
    while 1:
        buttons_pressed = joystick.get_and_clear_button_press_history()
        # Read the x and y axes of the left hand stick, the right hand stick has axes 2 and 3
        x = joystick.axes[0].corrected_value()
        y = joystick.axes[1].corrected_value()
        c = x * 90
        a = 90 - c
        print(x,y,a)
        angle = a
        if buttons_pressed & 1 << SixAxis.BUTTON_SQUARE:
            PWM.stop(servo_pin)
            PWM.cleanup()
            break
        angle_f = float(angle)
        duty = 100 - ((angle_f / 180) * duty_span + duty_min) 
        PWM.set_duty_cycle(servo_pin, duty)
        
       