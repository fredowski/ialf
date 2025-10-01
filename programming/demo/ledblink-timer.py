from machine import Pin, Timer

# Use the timer to call a function periodically
# Show again blinking leds

# The onboard led
onboardled = Pin("LED", Pin.OUT)

# D2 on Racershield v1.2
led2 = Pin(2, Pin.OUT)

timer = Timer()

# This function is called whenever the timer expires
def blink(timer):
    led2.toggle()
    onboardled.toggle()

# Setup the timer with a frequency of 2.5 Hz
timer.init(freq=2.5, mode=Timer.PERIODIC, callback=blink)
