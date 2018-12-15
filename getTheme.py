#!/usr/bin/env python3
"""Get the settings from time of day to set the right theme."""

import subprocess as sp
from generators import get
from generators import set
from PIL import Image

if __name__ == "__main__":

    bgLoc = get.getBg()
    bgImg1 = Image.open(bgLoc[1]).convert('RGB')
    bgImg2 = Image.open(bgLoc[2]).convert('RGB')

    rgbcolors = get.colorList(bgImg1)
    rgbcolors = get.colorList(bgImg2)

    for rgbcolor in rgbcolors:
        hexdict = get.makeHexDict(rgbcolor)
    hexlist = get.makeHexList(hexdict)

    set.conkyDefault(hexlist)
    setBg = sp.run(set.fehBg(bgLoc))
