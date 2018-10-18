#!/usr/bin/env python3
"""Get the settings from time of day to set the right theme."""

from generators import colorgen
import sys
import os
from PIL import Image

if __name__ == "__main__":

    imgLocation = sys.argv[1]
    imgFolder = os.path.split(imgLocation)[0]
    img = Image.open(imgLocation).convert('RGB')

    hexdict = {}
    colorgen.populate_dictionary(hexdict, img)
    hexlist = sorted(hexdict, key=hexdict.get, reverse=True)
    print(hexlist[:16])
