# microbit_analog_servo_SG90-micropython

##### Copying the module:

1. Save [the module](https://github.com/microbit-playground/microbit-servo-class/blob/master/servo.py) to your computer.

2. Copy the downloaded module to the `/mu_code/` directory in the root of your home directory.

3. Flash your program to mu.

4. An error message will scroll across the screen about the lack of the servo module.

5. Once it has finished, click the 'files' icon in mu and upload the `servo.py` file to your microbit.

6. Press reset on your microbit. When the program runs again it will load the module.

##### In your program:

```
  
from microbit import *
from Servolib import *

while True:
    angle = 0
    for angle in range(180):
        Servolib.set_servo_angle(pin2, angle)
        print(angle)
        sleep(200)
```
