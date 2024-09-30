from machine import Pin, PWM
from time import sleep

ledpin = Pin(25, Pin.OUT)
ml1 = Pin(13, Pin.OUT)
ml2 = Pin(12, Pin.OUT)
mr1 = Pin(11, Pin.OUT)
mr2 = Pin(10, Pin.OUT)

motorpwm = PWM(ml1)
ledpwm = PWM(ledpin)
ml2.low()

ledpwm.freq(1000)
ledpwm.duty_u16(20000)
motorpwm.freq(500)

dutycycle=32000


while True:
    motorpwm.duty_u16(dutycycle)
    ledpwm.duty_u16(dutycycle)
    dutycycle = (dutycycle + 1000) % 65535
    print(dutycycle)
    sleep(0.2)

    
    


