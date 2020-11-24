from raspledstrip.ledstrip import *
from time import sleep


led = LEDStrip(32, True)

while True:

    try:
        for r in range(0,255):
            led.fillRGB(r,0,0)
            led.update()
            print(r)
            sleep(0.1)

        for g in range(0,255):
            led.fillRGB(r,g,0)
            led.update()
            print(g)
            sleep(0.1)

        for b in range(0,255):
            led.fillRGB(r,g,b)
            led.update()
            print(b)
            sleep(0.1)

    except KeyboardInterrupt:
        led.all_off()
        exit()

