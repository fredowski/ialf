from machine import Pin
from time import sleep

# Blink the ialed board connected via Seeed Grove Cable

# ialed v0.2 connected to D16 grove connector on Racershield v1.2
# That grove connector is routed to GPIO16 (GPIO17 = secondary)
# ialed v0.2 has the additional red led connected to the secondary
# seeed grove connector pin.
ialed = Pin (16, Pin.OUT)
ialedred = Pin (17, Pin.OUT)

while True:
    # white off, red on for 1 second
    ialed.low()
    ialedred.high()
    sleep(1)
    # white on, red off for 2 seconds
    ialed.high()
    ialedred.low()
    sleep(2)
    # both off for one second
    ialed.low()
    ialedred.low()
    sleep(1)
