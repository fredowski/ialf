from machine import Pin, PWM
from time import sleep

# Den linken Motor mit PWM ansteueren
# Voll, Mittel, Langsam, Aus
# Die LEDs D2 und D3 zeigen den Modus an

# LED D2 auf dem Racershield v1.2
led2 = Pin(2, Pin.OUT)
# LED D3 connected to GPIO 3 on Racershield v1.2
led3 = Pin(3, Pin.OUT)
# Motorsteuerleitungen auf dem Racershield
ml1 = Pin(13, Pin.OUT)
ml2 = Pin(12, Pin.OUT)
mr1 = Pin(11, Pin.OUT)
mr2 = Pin(10, Pin.OUT)

# Rechten Motor ausschalten
mr1.low()
mr2.low()

# Die Steuerleitung 2 vom linken Motor wird
# mit dem PWM zwischen 0 und 1 geschaltet
motorpwm = PWM(ml2)
# Die Steuerleitung 1 vom linken Motor ist high
ml1.high()

# Mit PWM Dutycycle 0 ist die Steuerleitung 2 permanent auf 0
# Damit läuft der Motor maximal VORWÄRTS
# Mit PWM Dutycycle 65535 ist die Steuerleitung 2 permanent auf 1
# Damit steht der Motor mit aktiver Bremse

# Wenn man die PWM Frequenz schnell genug macht (15000 Hz) dann
# fliesst der Motorstrom während des Leitungszustands "Bremse" wegen der
# Induktivität weiter. 

# PWM Frequenz 15000 Hz
motorpwm.freq(15000)

while True:
    # Voll AN
    motorpwm.duty_u16(0)
    led2.high()
    led3.high()
    sleep(3)
    # ca. Halb AN
    motorpwm.duty_u16(30000)
    led2.high()
    led3.low()
    sleep(3)
    # Ein bisschen an
    motorpwm.duty_u16(55000)
    led2.low()
    led3.high()
    sleep(3)
    # Motor aus 
    motorpwm.duty_u16(65535)
    led2.low()
    led3.low()
    sleep(3)
