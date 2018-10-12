#!/usr/bin/env python3
"""Read through an image and return the 16 most dominant color values."""

import os
import sys
from PIL import Image


def rgb_to_hex(r, g, b):
    """Convert rgb output values to hex values."""
    return '#%02x%02x%02x' % (r, g, b)


def populate_dictionary(hexvalue):
    """Read the image and populate the dictionary with unique hexvalues."""
    for x in range(width):
        for y in range(height):
            r, g, b = _img.getpixel((x, y))
            hexvalue = (rgb_to_hex(r, g, b))
            if hexvalue not in hexdict:
                hexdict[hexvalue] = int(0)
            hexdict[hexvalue] += 1


_imgLocation = sys.argv[1]
_imgFolder = os.path.split(_imgLocation)[0]
_img = Image.open(_imgLocation).convert('RGB')
width, height = _img.size

hexdict = {}

if __name__ == "__main__":

    populate_dictionary(hexdict)
    hexlist = sorted(hexdict, key=hexdict.get, reverse=True)
    print(hexdict)
    print(hexlist[:16])
