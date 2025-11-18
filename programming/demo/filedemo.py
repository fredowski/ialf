from machine import Pin, ADC
from time import ticks_us, ticks_diff
from array import array

# Show the influence of the dcdc mode pfm vs pwm on the
# ADC readings. pfm mode introduces a ripple on the
# 3.3V supply line. Switching to pwm will reduce the ripple
# This measurement of the ialightsens sensor shows the effect
# on the ADC input

# ialed v0.2 connected to D16 grove connector on Racershield v1.2
# That grove connector is routed to GPIO16 (GPIO17 = secondary)
# ialed v0.2 has the additional red led connected to the secondary
# seeed grove connector pin.
ialed = Pin (16, Pin.OUT)
iaredled = Pin (17, Pin.OUT)
ialed.on()
iaredled.off()

# The dcdc voltage converter RT6154 on the Pi Pico 2 can operate in two modes
# controlled via the PS/SYNC pin which is connected to WL_GPIO1 on the Wifi chip
# PS = 0: PFM mode - default - high ripple at light loads
# PS = 1: PWM mode - less ripple but worse efficiency in light loads
dcdcmode = Pin ("WL_GPIO1", Pin.OUT)
dcdcmode.off()

# ialightsens v0.1 connected to seeed grove connector A1 via cable
# Grove connector A1 is routed to GP27 as primary and
# GP26 as secondary pin
adc = ADC(Pin(27))

# The SAR ADC on the RP2350 can sample with 500 kSamples/s, corresponding to one sample
# every 2 us. We want to run a little bit slower. Due to execution time of the python
# code we measure to whole loop time. From that we can estimate the actual sample rate.

# Create an array with space for 10000 samples
mv = array('H',range(10000))

# Store the start time just before the sampling loop
start = ticks_us()

# Run in default PFM mode and fill half of the array
# Expect higher ripple resulting in higher noise
for i in range(len(mv)):
    lsval = adc.read_u16()
    mv[i] = lsval
   
# Sampling is finished. Now store the time difference
# When I did this it took 133920 us for 10000 samples, i.e. 13.4 us per sample
# This translates to a sampling frequency of 74 kSamples/s
# So the sampling of 10000 samples takes around 130 ms
    
diff = ticks_diff(ticks_us(),start);
print("Sample in usec: ", diff);

f = open("log.txt", "w")
start = ticks_us()
for a in mv:
    print(a, file=f)
diff = ticks_diff(ticks_us(), start)
f.close()

# This took 964000 us for me, i.e 964ms to write 10000 lines
print("Zeit für Schreiben in usec: ", diff);