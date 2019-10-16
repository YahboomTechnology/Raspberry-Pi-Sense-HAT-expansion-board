#!/usr/bin/python
import time
from sense_hat import SenseHat
import pygame
from pygame.locals import *

sense = SenseHat()
# color value of display
X = (0, 0, 255)
O = (0, 0, 0)

# Smile expression data
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
# Arrow pattern
point = [
    O, O, O, X, X, O, O, O,
    O, O, X, X, X, X, O, O,
    O, X, X, X, X, X, X, O,
    X, X, X, X, X, X, X, X,
    O, O, O, X, X, O, O, O,
    O, O, O, X, X, O, O, O,
    O, O, O, X, X, O, O, O,
    O, O, O, X, X, O, O, O
]

# Initialize pygame and display（640*480）window
running = True
pygame.init()
pygame.display.set_mode((640, 480))

# Display arrow pointing according to the direction of the rocker
def handle_event(event):
    if event.key == pygame.K_DOWN:
        sense.set_rotation(180)
        sense.set_pixels(point)
    elif event.key == pygame.K_UP:
        sense.set_rotation(0)
        sense.set_pixels(point)
    elif event.key == pygame.K_LEFT:
        sense.set_rotation(270)
        sense.set_pixels(point)
    elif event.key == pygame.K_RIGHT:
        sense.set_rotation(90)
        sense.set_pixels(point)
    elif event.key == pygame.K_RETURN:
        sense.clear()
        sense.set_rotation(0)
        sense.set_pixels(smile)
    time.sleep(0.5)

# Judge the rocker operation
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            handle_event(event)
        if event.type == KEYUP:
            sense.clear()
