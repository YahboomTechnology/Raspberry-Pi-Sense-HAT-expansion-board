#!/usr/bin/python
from sense_hat import SenseHat

sense = SenseHat()

# Set the direction of rotation (0,90,180,270 for choice), default is 0
sense.set_rotation(180)

# Set color R G B value
color_text = (0, 0, 255)
color_back = (0, 0, 0)


while True:
    # Obtain the atmospheric pressure value on the sensor. 
    # pressure = sense.pressure
    pressure = sense.get_pressure()

    # The terminal prints out the atmospheric pressure value and saves two decimal places.
    print("Pressure: %0.2f Millibars" % pressure)

	# The parameter scroll_speed changes the scrolling speed, the default is 0.1, 
	# text_colour is the font color , and back_colour is the background color.
    sense.show_message("Pressure=%0.2fmbar" % pressure, scroll_speed=0.05,
                       text_colour=color_text, back_colour=color_back)
