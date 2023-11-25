# micropython-color-wheel
Color changers for Neopixel / WS2812 LED Strips / rings. 

If your Neopixel is of the 5V type, onnect the Neopixel ring to power with any of the GND pins (3,8,13,18,23,33 or 38) on the Raspberry Pi Pico and the DataIN in the code here is connected to GPIO 1. 

For LEDs with higher voltage you need to provide external power. 

1. simple-color-change.py changes all leds in the strip at once in the same colour.
2. color-chaser.py changes colours sequentially in the LEDs your ring has. 
