#!/usr/bin/env python3
"""Get the settings from time of day to set the right theme."""

import subprocess as sp
from generators import get
from generators import set
from PIL import Image

if __name__ == "__main__":

#    bgLoc = get.getBg()
    bgLoc = ['/Users/jorn/Downloads/wallpapers/inputfiles/dusk/she_is_the_bad_one_by_kvacm-dbttlc1.jpg']

    for bgImg in bgLoc:
        bgOpened = Image.open(bgImg).convert('RGB')
        rgbcolors = get.colorList(bgOpened)

    for rgbcolor in rgbcolors:
        hexdict = get.makeHexDict(rgbcolor)
    hexlist = get.makeHexList(hexdict)

    set.conkyColors(hexlist)
#    setBg = sp.run(set.fehBg(bgLoc))
    set.gtkColors(hexlist)