from machine import Pin

# Beide Motoren ausschalten

# LED D2 auf dem Racershield v1.2
led2 = Pin(2, Pin.OUT)
# LED D3 auf dem Racershield v1.2
led3 = Pin(3, Pin.OUT)
# Motorsteuerleitungen auf dem Racershield
ml1 = Pin(13, Pin.OUT)
ml2 = Pin(12, Pin.OUT)
mr1 = Pin(11, Pin.OUT)
mr2 = Pin(10, Pin.OUT)

# Ausschalten
led2.low()
led3.low()
ml1.low()
ml2.low()
mr1.low()
mr2.low()
