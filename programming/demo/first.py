from machine import Pin
from time import sleep

# The "Hello World" in embedded is the blinking led...

# Pi Pico Onboard LED. There is a lot of magic behind this
# as the onboard led on a Pi Pico W is not attached directly
# to the RP2350 but to the Infineon CYW43439 Wifi module.
led = Pin("LED", Pin.OUT)

while True:
    led.toggle()
    sleep(1)


