from machine import Pin, ADC
from time import sleep

# Test the ialightsens sensor with the ialed white led
# ialed v0.1 connected to D16 grove connector on Racershield v1.2
# That grove connector is routed to GPIO16 (GPIO17 = secondary)
ialed = Pin (16, Pin.OUT)

# ialightsens v0.1 connected to seeed grove connector A1 via cable
# Grove connector A1 is routed to GP27 as primary and
# GP26 as secondary pin
adc = ADC(Pin(27))

# I use the onboard led D2 on Raceshield v1.2 to test on/off
# The LED D2 is routed to GPIO2 on the Raceshield v1.2 board
boardled = Pin(2, Pin.OUT)

# Switch on the ialed connected to D16 seeed grove connector
ialed.on()

# Read the lightsensor value via ADC, compare the value to 5000
# and loop

while True:
    lsval = adc.read_u16()
    if (lsval > 5000):
        boardled.on()
    else:
        boardled.off()
    print(lsval)
    sleep(0.1)
