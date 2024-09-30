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


while True:
    motorpwm.duty_u16(65535)
    ledpwm.duty_u16(65535)
    sleep(10)
    motorpwm.duty_u16(30000)
    ledpwm.duty_u16(30000)
    sleep(10)
    motorpwm.duty_u16(10000)
    ledpwm.duty_u16(10000)
    sleep(10)
    motorpwm.duty_u16(0)
    ledpwm.duty_u16(0)
    sleep(3)
    
    


