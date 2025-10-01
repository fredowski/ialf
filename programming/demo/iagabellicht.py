from machine import Pin
from time import sleep

# Test iagabel Gabellichtschranke
# Die Gabellichtschranke hat zwei unabhängige Lichtschranken
# Der Zustand der Pins wird auf den beiden Racershield LEDs
# ausgegeben.

# LED D2 connected to GPIO 2 on Racershield v1.2
led2 = Pin(2, Pin.OUT)
# LED D3 connected to GPIO 3 on Racershield v1.2
led3 = Pin(3, Pin.OUT)

# Gabel v0.1 attached to I2C0 grove connector on Racershield v1.2
p8 = Pin(8, Pin.IN)
p9 = Pin(9, Pin.IN)

while True:
    p8val = p8.value()
    print(p8val)
    if p8val == 1:
        led2.high()
    else:
        led2.low()
    p9val = p9.value()
    if p9val == 1:
        led3.high()
    else:
        led3.low()
    sleep(0.01)
