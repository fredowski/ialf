from machine import Pin, PWM
from time import sleep

# Motoren langsam fahren lassen mit PWM
# Dazu kurzen Anfahrstrom geben, damit der Motor
# loslaeuft.

# LED D2 connected to GPIO 2 on Racershield v1.2
led2 = Pin(2, Pin.OUT)
# LED D3 connected to GPIO 3 on Racershield v1.2
led3 = Pin(3, Pin.OUT)

# Motorsteuerleitung für den Motortreiber DRV8835
# auf dem Racershield
ml1 = Pin(13, Pin.OUT)
ml2 = Pin(12, Pin.OUT)
mr1 = Pin(11, Pin.OUT)
mr2 = Pin(10, Pin.OUT)

# Motoren in PWM
motorpwml = PWM(ml1)
ml2.high()
motorpwmr = PWM(mr1)
mr2.high()

# PWM Frequenz ausreichend hoch, damit der Strom in der
# Kurzschlussphase weiterfliessen kann
freq = 30000
motorpwml.freq(freq)
motorpwmr.freq(freq)

for i in range(100):
    # Anfahren mit höherem Strom
    motorpwml.duty_u16(30000)
    motorpwmr.duty_u16(30000)
    led2.high()
    led3.low()
    sleep(0.01)
    # Jetzt mit minimaler Leistung weiter
    motorpwml.duty_u16(50000)
    motorpwmr.duty_u16(50000)
    led2.low()
    led3.high()
    sleep(4)
    # Motor AUS
    motorpwml.duty_u16(65535)
    motorpwmr.duty_u16(65535)
    led2.low()
    led3.low()
    sleep(1)
