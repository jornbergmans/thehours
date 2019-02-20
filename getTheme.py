#!/usr/bin/env python3
"""Get the settings from time of day to set the right theme."""

from generators import get
from generators import set
from PIL import Image

if __name__ == "__main__":

    # bgLoc = get.getBg()
    currentThemeConfigPath = set.currentThemeConfigPath
    bgLoc = get.getBg()

    rgbcolorlist = []
    for bgImg in bgLoc:
        bgOpened = Image.open(bgImg).convert('RGB')
        rgbcolors = rgbcolorlist.extend(get.colorList(bgOpened))
    for rgbcolor in rgbcolorlist:
        hexdict = get.makeHexDict(rgbcolor)
    hexlist = get.makeHexList(hexdict)
    print(hexlist)

    # Setting these prints the values to their respective output files
    set.conkyColors(hexlist)
    set.gtkColors(hexlist)
    set.obColors(hexlist)
    with open(currentThemeConfigPath + 'feh/.fehbg', 'w') as feh_output:
        fehcmd = set.fehBg(bgLoc)
        feh_output.write("#!/bin/sh" + "\n")
        for item in fehcmd:
            #fehlist = print("'" + item + "'", end=' ')
            feh_output.write("'" + item + "' ")
