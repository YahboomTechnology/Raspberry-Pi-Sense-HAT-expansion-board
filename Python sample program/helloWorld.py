#!/usr/bin/python
from sense_hat import SenseHat

sense = SenseHat()

#Set the direction of rotation (0,90,180,270 for choice),default is 0
sense.set_rotation(180)

#Set color R G B value
color_text = (0, 0, 255)
color_back = (0, 0, 0)

#sense.show_message("Hello World!")

#The parameter scroll_speed changes the scrolling speed, the default is 0.1, 
#text_colour is the font color of the display, 
#and back_colour is the background color.
sense.show_message("Hello World!", scroll_speed=0.05, text_colour=color_text, back_colour=color_back)

