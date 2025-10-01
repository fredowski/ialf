from machine import Pin
from time import sleep

# Blink the pico onboard led,
# the two Racershield leds D2 and D2
# a led attached to D16 Seeed Grove connector

# Pi Pico Onboard LED. There is a lot of magic behind this
# as the onboard led on a Pi Pico W is not attached directly
# to the RP2350 but to the Infineon Wifi module.
led = Pin("LED", Pin.OUT)
# LED D2 connected to GPIO 2 on Racershield v1.2
led2 = Pin(2, Pin.OUT)
# LED D3 connected to GPIO 3 on Racershield v1.2
led3 = Pin(3, Pin.OUT)

# Attach the ialed or seeed led to D16 grove connector
# on Racershield v1.2
groveled = Pin(16, Pin.OUT)

while True:
    led.toggle()
    led2.toggle()
    led3.toggle()
    groveled.toggle()
    sleep(1)
