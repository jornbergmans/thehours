#!/usr/bin/env python3
"""Get the settings from time of day to set the right theme."""

from generators import get
from generators import set
import sys
import os
import re
from PIL import Image

if __name__ == "__main__":

    bgLoc = get.currentBg()
    print('FEH WILL GET IMAGE LOCATION FROM ' + str(bgLoc))
    fehcmd = set.fehfunct()
#    sp.run(fehcmd)
    print('FEH WILL RUN AS: ' + str(fehcmd))
    print('FEHBG WILL BE MOVED TO: ' + "os.rename(get.home + '/.fehbg', get.currentThemeBG + '/.fehbg')")

#    imgFolder = os.path.split(bgLoc)[0]
    img = Image.open(bgLoc).convert('RGB')

    rgbcolors = get.colorList(img)

    for rgbcolor in rgbcolors:
        hexdict = get.makeHexDict(rgbcolor)
    hexlist = get.makeHexList(hexdict)
    print(hexlist)

    set.conkyDefault(hexlist)

#    reghex = re.compile('\#[a-z0-9]*')
#    conkyDefaultColor = generator.conkyDefault()
#    conkyNewDefault = re.sub(reghex, hexlist[0], conkyDefaultColor, 1)
#    conkyWindowColor = generator.conkyWindow()
#    conkyNewWindow = re.sub(reghex, hexlist[1], conkyWindowColor, 1)
