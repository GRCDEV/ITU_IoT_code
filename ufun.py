# Some useful functions "ufun":

import random
import time

OFF = 'OFF'

def get_data_from_sensor(sensor_id="RAND"):
    if sensor_id == "RAND":
        return random.randint(0,100)

def set_led_to(color='GREEN'):
    print("LED set to: ", color)

def flash_led_to(color='GREEN', t1=1):
    set_led_to(color)
    time.sleep(t1)
    set_led_to(OFF)
