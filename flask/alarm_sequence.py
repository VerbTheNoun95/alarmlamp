from raspledstrip.ledstrip import *
from time import sleep


led = LEDStrip(32, True)

def sequence(wait=0.01):

    for r in range(0,256):
        led.fillRGB(r,0,0)
        led.update()
        #print(f"Red: {r}")
        sleep(wait)

    for g in range(0,256):
        led.fillRGB(r,g,0)
        led.update()
        #print(f"Green: {g}")
        sleep(wait)

    for b in range(0,256):
        led.fillRGB(r,g,b)
        led.update()
        #print(f"Blue: {b}")
        sleep(wait)

    input("Please turn off the lights")
    off()

def off():
    led.fillRGB(0,0,0)
    led.update()

if __name__ == "__main__":
    sequence()

