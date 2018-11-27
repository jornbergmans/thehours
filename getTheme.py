#!/usr/bin/env python3
"""Get the settings from time of day to set the right theme."""

from generators import generator
import sys
import os
import re
from PIL import Image

if __name__ == "__main__":

    fehcmd = generator.fehfunct()
#    sp.run(fehcmd)
    print('FEH WILL RUN AS: ' + str(fehcmd))
    print('FEHBG WILL BE MOVED TO: ' + "os.rename(generator.home + '/.fehbg', generator.currentThemeBG + '/.fehbg')")

    bgLoc = generator.currentBg()
    imgFolder = os.path.split(bgLoc)[0]
    img = Image.open(bgLoc).convert('RGB')

    rgbcolors = generator.colorList(img)

    for rgbcolor in rgbcolors:
        hexdict = generator.makeHexDict(rgbcolor)
    hexlist = sorted(hexdict, key=hexdict.get, reverse=False)
    nth = int(len(hexlist) / 16)
    hexToUse = hexlist[0::nth]

#    reghex = re.compile('\#[a-z0-9]*')
#    conkyDefaultColor = generator.conkyDefault()
#    conkyNewDefault = re.sub(reghex, hexlist[0], conkyDefaultColor, 1)
#    conkyWindowColor = generator.conkyWindow()
#    conkyNewWindow = re.sub(reghex, hexlist[1], conkyWindowColor, 1)
