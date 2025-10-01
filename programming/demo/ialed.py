from machine import Pin
from time import sleep

# Blink the ialed board connected via Seeed Grove Cable

# ialed v0.1 connected to D16 grove connector on Racershield v1.2
# That grove connector is routed to GPIO16 (GPIO17 = secondary)
ialed = Pin (16, Pin.OUT)

while True:
    ialed.high()
    sleep(1)
    ialed.low()
    sleep(1)
