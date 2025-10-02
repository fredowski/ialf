from machine import Pin
from time import sleep

# Test the Seeed Linefinder on the Racershield
# https://www.seeedstudio.com/Grove-Line-Finder-v1-1.html
# Connect to port Connector D20 and the Racershield
# which translates to pin 20 on the Pi Pico

# Then linefinder has a comparator and gives  digital output
# depending on the poti setting on the board.

# Linefinder digital input
lf = Pin(20, Pin.IN)

# Pico onboard LED magic
led = Pin("LED", Pin.OUT)

while True:
    lfval = lf.value()
    print(lfval)
    # Negative logic. When the led on the linefinder is on,
    # the digital output is low = 0.
    if lfval == 1 :
        led.on()
    else :
        led.off()
    sleep(0.1)
