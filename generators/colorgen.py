#!/usr/bin/env python3
"""Read through an image and return the 16 most dominant color values."""

import os
import sys
from PIL import Image


def rgb_to_hex(r, g, b):
    """Convert rgb output values to hex values."""
    return '#%02x%02x%02x' % (r, g, b)


def populate_dictionary(hexdict, img):
    """Read the image and populate the dictionary with unique hexvalues."""
    width, height = img.size
    colors = []
    for x in range(width):
        for y in range(height):
            r, g, b = img.getpixel((x, y))
            colors.append([r, g, b])
            hexvalue = (rgb_to_hex(r, g, b))
            if hexvalue not in hexdict:
                hexdict[hexvalue] = int(0)
            hexdict[hexvalue] += 1


def colorsort():
    """Sort colorvalues by HSL."""
    colors.sort(key=lambda rgb: colorsys.rgb_to_hsv(*rgb) )

