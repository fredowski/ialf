from machine import Pin
from time import sleep

# Motortest mit dem Motortreiber DRV8835
# von Texas Instruments auf dem Racershield
# Dazu die Motoren und die Batterie anschliessen
# Die Motoren laufen nur mit Batterie - USB reicht nicht

# Bei AUS Rollen rollen die Motoren ungebremst aus
# Bei AUS Bremse sind die Motoren kurzgeschlossen und bremsen

# LED D2 auf dem Racershield v1.2
led2 = Pin(2, Pin.OUT)
# LED D3 auf dem Racershield v1.2
led3 = Pin(3, Pin.OUT)
# Motorsteuerleitungen auf dem Racershield
ml1 = Pin(13, Pin.OUT)
ml2 = Pin(12, Pin.OUT)
mr1 = Pin(11, Pin.OUT)
mr2 = Pin(10, Pin.OUT)

while True:
    # Beide Motoren AN Vorwärts
    led2.high()
    led3.low()
    ml1.high()
    ml2.low()
    mr1.high()
    mr2.low()
    sleep(10)
    # Beide Motoren AUS Rollen
    led2.low()
    led3.low()
    mr1.low()
    mr2.low()
    ml1.low()
    ml2.low()
    sleep(3)
    # Beide Motoren AN Rückwärts
    led2.low()
    led3.high()
    ml1.low()
    ml2.high()
    mr1.low()
    mr2.high()
    sleep(10)
    # Beide Motoren AUS Bremse
    led2.high()
    led3.high
    ml1.high()
    ml2.high()
    mr1.high()
    mr2.high()
    sleep(3)
