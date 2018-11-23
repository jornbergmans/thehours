#!/usr/bin/env python3
"""Get the settings from time of day to set the right theme."""

from generators import colorgen
import sys
import os
import re
from PIL import Image

if __name__ == "__main__":

    fehcmd = colorgen.fehfunct()
    print(fehcmd)
    os.rename
    bgLoc = colorgen.currentBg()
    print(bgLoc)

    imgFolder = os.path.split(bgLoc)[0]
    print(imgFolder)
    img = Image.open(bgLoc).convert('RGB')

    print(img)
    rgbcolors = colorgen.colorList(img)
    hslcolors = colorgen.hslSort(rgbcolors)
    print(hslcolors)

    for rgbcolor in rgbcolors:
        hexdict = colorgen.makeHexDict(rgbcolor)
    print(hexdict)

    hexlist = sorted(hexdict, key=hexdict.get, reverse=True)
    print(hexlist[:16])


    reghex = re.compile('\#[a-z0-9]*')
    conkyDefaultColor = colorgen.conkyDefault()
    conkyNewDefault = re.sub(reghex, hexlist[0], conkyDefaultColor, 1)
    conkyWindowColor = colorgen.conkyWindow()
    conkyNewWindow = re.sub(reghex, hexlist[1], conkyWindowColor, 1)
