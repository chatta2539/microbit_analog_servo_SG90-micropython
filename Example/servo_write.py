from microbit import *
from Servolib import *

while True:
    angle = 0
    for angle in range(180):
        Servolib.set_servo_angle(pin2, angle)
        print(angle)
        sleep(200)
