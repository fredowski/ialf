from machine import Pin
from time import sleep

lf = Pin(20, Pin.IN)

while True:
    lfval = lf.value()
    print(lfval)
    sleep(0.1)
