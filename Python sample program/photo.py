#!/usr/bin/python
from sense_hat import SenseHat

sense = SenseHat()

#Set the direction of rotation (0,90,180,270 for choice),default is 0
sense.set_rotation(180)

#clear display
sense.clear()
#Display pictures, pictures need to be placed in the same folder
sense.load_image("space_invader.png")
