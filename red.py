from raspledstrip.ledstrip import *
from time import sleep


led = LEDStrip(32, True)

while True:

    try:
        for i in range(0,255):
            led.fillRGB(i,0,0)
            led.update()
            print(i)
            sleep(0.2)

        for b in range(0,255):
            led.fillRGB(i,0,b)
            led.update()
            print(b)
            sleep(0.5)

        for j in range(1,255):
            red = 255 - j
            led.fillRGB(red, 0, 0)
            led.update()
            print(red)
            sleep(0.3)

    except KeyboardInterrupt:
        led.all_off()
        exit()

