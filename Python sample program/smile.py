#!/usr/bin/python
from sense_hat import SenseHat

sense = SenseHat()
#Display color value
X = (0, 255, 0)
O = (0, 0, 0)

#Data of smile
smile = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, X, O, O, X, O, O,
    O, O, O, O, O, O, O, O,
    O, X, O, O, O, O, X, O,
    O, O, X, X, X, X, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O
]

#Display smile
sense.set_pixels(smile)
