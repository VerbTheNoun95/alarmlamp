from raspledstrip.ledstrip import *
from time import sleep
from gpiozero import Button


led = LEDStrip(32, True)
button = Button(2)

def sequence(wait=0.1):

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

    print("Please turn off the lights")
    button.wait_for_press()
    print("Turning off...")
    off()
    #while True:
    #    try:
    #        off()
    #        sleep(1)
    #    except KeyboardInterrupt:
    #        break

def off():
    led.fillRGB(0,0,0)
    led.update()

if __name__ == "__main__":
    sequence(wait=0.05)
    led.all_off()

