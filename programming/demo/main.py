from machine import Pin, Timer
led = Pin(25, Pin.OUT)
groveled = Pin(18, Pin.OUT)
i = 1;

timer = Timer()

def blink(timer):
    groveled.toggle()
    led.toggle()
    
timer.init(freq=2.5, mode=Timer.PERIODIC, callback=blink)



