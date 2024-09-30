from machine import Pin, PWM
from time import sleep

ledpin = Pin(25, Pin.OUT)
ml1 = Pin(13, Pin.OUT)
ml2 = Pin(12, Pin.OUT)
mr1 = Pin(11, Pin.OUT)
mr2 = Pin(10, Pin.OUT)

motorpwml = PWM(ml1)
motorpwmr = PWM(mr1)

freq = 20
motorpwml.freq(freq)
motorpwmr.freq(freq)

dutycycle = 10000

for i in range(100):
    motorpwml.duty_u16(dutycycle)
    motorpwmr.duty_u16(dutycycle)
    sleep(1)
    motorpwml.duty_u16(0)
    motorpwmr.duty_u16(0)
    sleep(1)

    
    


