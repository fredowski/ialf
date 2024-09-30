from machine import Pin, ADC, Timer
from time import sleep

groveled = Pin(18, Pin.OUT)
boardled = Pin(25, Pin.OUT)
adc = ADC(Pin(28))

timer = Timer()

def blink(timer):
    groveled.toggle()
    
timer.init(freq=2.5, mode=Timer.PERIODIC, callback=blink)

while True:
    lsval = adc.read_u16()
    if (lsval > 5000):
        boardled.on()
    else:
        boardled.off()
    print(lsval)
    sleep(0.1)

