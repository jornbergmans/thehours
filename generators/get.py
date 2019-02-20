#!/usr/bin/env python3
"""Read through an image and return the 16 most dominant color values."""

import subprocess as sp
import os
import datetime
import sys

now = int(datetime.datetime.now().strftime('%H'))
home = os.path.expanduser('~')


# Setting the first part - what time is it?
def bgHour():
    """Return the name of the theme we are setting based on the current time."""
    if 0 <= now <= 6:
        theHour = 'dark'
    elif 6 <= now <= 12:
        theHour = 'dawn'
    elif 12 <= now <= 18:
        theHour = 'day'
    elif 18 <= now <= 23:
        theHour = 'dusk'
    return theHour


# Use specified theme, or if not specified, our theme will be set to the current hour0
if sys.argv[1] in ['dusk', 'day', 'dawn', 'dark']:
    currentTheme = sys.argv[1]
else:
    currentTheme = bgHour()
currentThemeBG = str(home + '/Pictures/Wallpapers/thehours/' + currentTheme)
currentThemeConf = str(home + '/.themes/thehours/configs/' + currentTheme)
# End setting the theme


# The function that reads what picture we'll be using for the theme
def getBg():
    """Make a random list of images from the current Hour."""
    feh_bgcmd = [
        '/usr/bin/env', 'feh',
        '--randomize',
        currentThemeBG,
        '-L', '%f']
    feh_list = sp.check_output(feh_bgcmd, )
    feh_list = feh_list.decode(sys.stdout.encoding)
    bgLoc = []
    bgLoc.append(feh_list.split()[0])
    bgLoc.append(feh_list.split()[1])
    return bgLoc


# Start reading the background image to get our output colors
def colorList(bgOpened):
    """Make a list of the rgb values of all the pixels."""
    width, height = bgOpened.size
    rgbcolors = []
    for x in range(width):
        for y in range(height):
            r, g, b = bgOpened.getpixel((x, y))
            rgbcolors.append([r, g, b])
    return rgbcolors


def rgbToHex(r, g, b):
    """Convert rgb output values to hex values."""
    return '#%02x%02x%02x' % (r, g, b)


hexdict = {}


def makeHexDict(rgbcolor):
    """Read the image and populate the dictionary with hexvalues
    and their brightness.
    """
    hexvalue = rgbToHex(rgbcolor[0], rgbcolor[1], rgbcolor[2])
    intvalue = int(rgbcolor[0] + rgbcolor[1] + rgbcolor[2])
    if hexvalue not in hexdict:
        hexdict[hexvalue] = intvalue
    return hexdict


def makeHexList(hexdict):
    """Read through the hex dict, sort it by luminance,
    and give the colors for our scheme."""
    fullhexlist = sorted(hexdict, key=hexdict.get, reverse=False)
    nth = int(len(fullhexlist) / 16)
    hexlist = fullhexlist[nth::nth]
    print(len(fullhexlist))
    print(nth)
    return hexlist
# End grabbing all the colors that we need for our theme
