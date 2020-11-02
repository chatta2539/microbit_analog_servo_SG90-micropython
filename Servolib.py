class Servolib:
    def set_servo_angle(pin, angle):
        duty = 26 + (angle * 102) / 180
        pin.write_analog(duty)