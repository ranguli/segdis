# segdis.py
# Author: Joshua Murphy, 2018
# GitHub: https://github.com/ranguli

# A program that visualizes a 7-segment display. It takes in a binary
# string, with each digit representing an on/off state for one of the
# segments 

import time
from graphics import *

window_width = 320
window_height = 240

window = GraphWin("Segment Display", window_width, window_height) 
window.setCoords(0, 0, window_width, window_height) 

digit_x1 = 50
digit_x2 = 120
digit_y1 = 120 
digit_y2 = 220

# This isn't pretty, unfortunately. Every segment of the display 
# is a Rectangle object defined by the graphics.py library. We must set 
# the position of each segment so that they line up properly.

center_segment = Rectangle(Point(digit_x1+10, digit_y1+50), Point(digit_x2-10, 180 ))
top_left_segment = Rectangle(Point(digit_x1 + 10,  digit_y1+90), Point(digit_x1 , 180))
bottom_left_segment = Rectangle(Point(digit_x1, digit_y1+10), Point(digit_x1 + 10, 170))
bottom_segment = Rectangle(Point(digit_x1 + 10, digit_y1+10), Point(digit_x2 - 10, (digit_y2/2)+10))
bottom_right_segment = Rectangle(Point(digit_x1+70, digit_y1+10), Point(digit_x1 + 60, 170))
top_right_segment = Rectangle(Point(digit_x1 + 70, digit_y1+60), Point(digit_x2 - 10, digit_y2-10))
top_segment = Rectangle(Point(digit_x1+10, digit_y1+90), Point(digit_x2-10, 220))

# This dictionary holds each segment of the display with a corresponding
# truth value. When a segment is set to true, it is illuminated on the 
# screen. When it it set to false, it does not illuminate.

segments = {
    bottom_left_segment: True,
    top_left_segment: True,
    bottom_segment: True,
    top_segment: True,
    center_segment: False,
    top_right_segment: True,
    bottom_right_segment: True
}

# Set the colour of all segments to red
for value in segments:
    value.setFill("red")

def getInput():
    validInput = False
    while not validInput:
        inputString = str(input("Enter a 7 digit binary string: \n" + "T C TL BL B BR TR \n"))
        inputString = list(inputString) 
        if (len(inputString) != 7):
            print("Try again.") 
        if (len(inputString) == 7):
            validInput = True 
            i = 0
            for key in segments:
                if inputString[i] == "0": 
                    segments[key] = False
                elif inputString[i] == "1":
                    segments[key] = True 
                i += 1

getInput()

while True:
    for segment, boolean in segments.items(): 
        segment.undraw()
        if (boolean is True):
            segment.draw(window) 
    getInput()
