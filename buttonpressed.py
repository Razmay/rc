from triangula.input import SixAxisResource, SixAxis
# Get a joystick as before
with SixAxisResource() as joystick:
    # No need for any button handlers, go straight into our loop
    while 1:
        buttons_pressed = joystick.get_and_clear_button_press_history()
        if buttons_pressed & 1 << SixAxis.BUTTON_TRIANGLE:
            print 'SQUARE pressed since last check'