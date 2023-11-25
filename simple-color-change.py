import neopixel
from machine import Pin
import time

# Raspberry Pi Pico pin where the Neopixel / WS2812 DataIN pin is connected
ws_pin = 0
# set the number of LEDs in your NeoPixel / WS2812 LED
led_num = 8
# Adjust the brightness as needed here: 
BRIGHTNESS = 0.1  # Adjust the brightness (0.0 - 1.0)
# Set the delay between color changes - The lower the number, the faster! 
DELAY = 0.01

neoRing = neopixel.NeoPixel(Pin(ws_pin), led_num)

scalar = float # a scale value (0.0 to 1.0)

# We use the HSV color space, as it's a 360º circle that seamlessly changes between almost the complete RGB color space
# This is our function to convert HSV to the RGB values needed by the MicroPython Neopixel library

def hsv_to_rgb( h:scalar, s:scalar, v:scalar, a:scalar ) -> tuple:
    a = int(255*a)
    if s:
        if h == 1.0: h = 0.0
        i = int(h*6.0); f = h*6.0 - i
        
        w = int(255*( v * (1.0 - s) ))
        q = int(255*( v * (1.0 - s * f) ))
        t = int(255*( v * (1.0 - s * (1.0 - f)) ))
        v = int(255*v)
        
        if i==0: return (v, t, w, a)
        if i==1: return (q, v, w, a)
        if i==2: return (w, v, t, a)
        if i==3: return (w, q, v, a)
        if i==4: return (t, w, v, a)
        if i==5: return (v, w, q, a)
    else: v = int(255*v); return (v, v, v, a)
    
while True:
    # we iterate through all 360 values in the HSV circle
    for i in range (0, 360, 1):
        rgb = hsv_to_rgb(i/360, 1.0, BRIGHTNESS, 1.0)
        color = rgb[0:3]
        neoRing.fill(color)
        neoRing.write()
        time.sleep(DELAY)
  
