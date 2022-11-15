from microbit import *

# init stop
pin0.write_analog(0)
pin1.write_analog(0)

while True:
    if button_a.is_pressed():
        pin0.write_analog(94)
        pin1.write_analog(50)
        sleep(3000)
    elif button_b.is_pressed():
        pin0.write_analog(50)
        pin1.write_analog(94)
        sleep(3000)
    else:
        pin0.write_analog(0)
        pin1.write_analog(0)
