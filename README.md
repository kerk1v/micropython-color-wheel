# micropython-color-wheel
Color changers for Neopixel / WS2812 LED Strips / rings. 

If your Neopixel is of the 5V type, connect the Neopixel ring to power with any of the GND pins (3,8,13,18,23,33 or 38) on the Raspberry Pi Pico and the DataIN in the code here is connected to GPIO 0. 

For LEDs with higher voltage you need to provide external power. 

1. simple-color-change.py changes all leds in the strip at once in the same colour.
2. color-chaser.py changes colours sequentially in the LEDs your ring has. 

## Why there is no white? 
I use "1" as the saturation value for all colours, so we're just circling around the external circumference of the HSV color model at full saturation, for simplicity's sake. White would be a saturation ("S") value of 0 in the HSV color model, a value of "S" = 1 moves us on the circumference of the color space. Values of "S" smaller than "1" move the point in the color model to the centre of the circle, decreasing saturation, pure white being "0" at any angle. 
