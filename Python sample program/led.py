#!/usr/bin/python
from sense_hat import SenseHat

sense = SenseHat()

#Set RGB color value
color = (255, 0, 0)
#Display a RGB light
sense.set_pixel(0,0,color)

#Another way of lighting(x,y,r,g,b)
#sense.set_pixel(0,0,255,0,0)

