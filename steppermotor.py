from bbpystepper import Stepper
import time


stp = Stepper()

stp.steps_per_rev = 4076
stp.rotate(360,10) # Rotates motor x *2 degrees at y RPM
