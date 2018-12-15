#!/usr/bin/env python3
"""Get the settings from time of day to set the right theme."""

import subprocess as sp
from generators import get
from generators import set
from PIL import Image

if __name__ == "__main__":

    bgLoc = get.getBg()
#    imgFolder = os.path.split(bgLoc)[0]
    img1 = Image.open(bgLoc[1]).convert('RGB')
    img2 = Image.open(bgLoc[2]).convert('RGB')

    rgbcolors = get.colorList(img1)
    rgbcolors = get.colorList(img2)

    for rgbcolor in rgbcolors:
        hexdict = get.makeHexDict(rgbcolor)
    hexlist = get.makeHexList(hexdict)
    # print(hexlist)

    set.conkyDefault(hexlist)
    setBg = sp.run(set.fehBg(bgLoc))


#    reghex = re.compile('\#[a-z0-9]*')
#    conkyDefaultColor = generator.conkyDefault()
#    conkyNewDefault = re.sub(reghex, hexlist[0], conkyDefaultColor, 1)
#    conkyWindowColor = generator.conkyWindow()
#    conkyNewWindow = re.sub(reghex, hexlist[1], conkyWindowColor, 1)
