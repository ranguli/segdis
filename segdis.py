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


# The order that you will see used continuously in the code is as follow.

# Center, Top Left, Bottom Left, Bottom, Top Right, Bottom Right, Top

# C	  TL	    BL		 B	 TR	    BR		  T
# 1st	  2nd	    3rd		 4th	 5th	    6th		  7th


# This is the order in which we iterate through the elements in the dictionary,
# informing what


center_segment = Rectangle(Point(digit_x1+10, digit_y1+50), Point(digit_x2-10, 180 ))
top_left_segment = Rectangle(Point(digit_x1 + 10,  digit_y1+90), Point(digit_x1 , 180))
bottom_left_segment = Rectangle(Point(digit_x1, digit_y1+10), Point(digit_x1 + 10, 170))
bottom_segment = Rectangle(Point(digit_x1 + 10, digit_y1+10), Point(digit_x2 - 10, (digit_y2/2)+10))
top_right_segment = Rectangle(Point(digit_x1 + 70, digit_y1+60), Point(digit_x2 - 10, digit_y2-10))
bottom_right_segment = Rectangle(Point(digit_x1+70, digit_y1+10), Point(digit_x1 + 60, 170))
top_segment = Rectangle(Point(digit_x1+10, digit_y1+90), Point(digit_x2-10, 220))

# This dictionary holds each segment of the display with a corresponding
# truth value. When a segment is set to true, it is illuminated on the 
# screen. When it it set to false, it does not illuminate.

segments = {

    center_segment: False,
    top_left_segment: False,
    bottom_left_segment: False,
    bottom_segment: False,
    top_right_segment: False,
    bottom_right_segment: False,
    top_segment: False
}

# Note these are *not* the binary representation of these decimal numbers,
# but the binary representation of what segments must be on/off to 
# represent the decimal number on screen.

decimal_lookup_table = {
    "0": "1110111",
    "1": "1100000",
    "2": "0111011",
    "3": "1111001",
    "4": "1101100",
    "5": "1011101",
    "6": "1011111",
    "7": "1110000",
    "8": "1111111",
    "9": "1111101" 
}



# Set the colour of all segments to red
for value in segments:
    value.setFill("red")


# Gets input from a String
def parseBits(inputString):
    if (len(inputString) == 7):
        i = 0
        for key in segments:
            if inputString[i] == "0": 
                segments[key] = False
            elif inputString[i] == "1":
                segments[key] = True 
            i += 1


def showOff():
    for key in decimal_lookup_table:
        inputString = decimal_lookup_table[key]
    for segment, boolean in segments.items():
        segment.undraw()
        if (boolean is True):
            segment.draw(window)


def drawDigit(segments):
    for segment, boolean in segments.items(): 
        if (boolean is True):
            segment.draw(window) 
        if (boolean is False):
            segment.undraw() 
        
def clearScreen():
    for segment, boolean in segments.items(): 
        segment.undraw() 
        
def main():
    # The graphics.py library doesn't appear to have a main loop, so we'll make our own.
    # All possible program states branch off and are dispatched by this main method.
   
    while True:
        inputString = str(input("Enter a 7 digit binary string: \n" + "C TL BL B BR TR T \n"))
        parseBits(inputString)
        clearScreen() 
        drawDigit(segments)
        print(segments.values())
main()
