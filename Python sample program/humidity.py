#!/usr/bin/python
from sense_hat import SenseHat

sense = SenseHat()

# Set the direction of rotation (0,90,180,270 for choice), default is 0
sense.set_rotation(180)

# Set color R G B value
color_text = (0, 0, 255)
color_back = (0, 0, 0)


while True:
    # Obtain the humidity value on the sensor. 
    humidity = sense.humidity
    # humidity = sense.get_humidity()

    # The terminal prints out the temperature value and saves two decimal places.
    print("Humidity: %0.2f %%RH" % humidity)

    # The parameter scroll_speed changes the scrolling speed, the default is 0.1, 
    # text_colour is the font color , and back_colour is the background color.
    sense.show_message("humidity=%0.2f%%RH" % humidity, scroll_speed=0.05,
                       text_colour=color_text, back_colour=color_back)
