#!/usr/bin/python3

from bibliopixel.layout import *
from bibliopixel.animation import StripChannelTest
from bibliopixel.drivers.SPI.LPD8806 import *


#create driver for a 32 pixels
driver = LPD8806(12, c_order=ChannelOrder.BRG)
led = Strip(driver)

anim = StripChannelTest(led)
anim.run()

