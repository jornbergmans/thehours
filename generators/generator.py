#!/usr/bin/env python3
"""Read through an image and return the 16 most dominant color values."""

import subprocess as sp
import re
import os
import sys
import colorsys
from PIL import Image
import datetime

theHour = int(datetime.datetime.now().strftime('%H'))
theHourTheme = ''
home = os.path.expanduser('~')
hexdict = {}

# Setting the first part - what time is it? 
def bgHour(bgHourDir):
    """Return the name of the theme we are setting based on the current time.."""
    if 0 <= theHour <= 6:
        theHourTheme = 'dark'
    elif 6 <= theHour <= 12:
        theHourTheme = 'dawn'
    elif 12 <= theHour <= 18:
        theHourTheme = 'day'
    elif 18 <= theHour <= 23:
        theHourTheme = 'dusk'
    return theHourTheme

### This means that our theme will be set to the current hour, like so
currentTheme = bgHour(theHourTheme)
currentThemeBG = str(home + '/.themes/thehours/backgrounds/' + bgHour(theHourTheme))
currentThemeConf = str(home + '/.themes/thehours/configs/' + bgHour(theHourTheme))
# End setting the theme


# All of the feh functions for selecting the backgrond we will use for the rest.
def fehfunct():
    """Build up the string to execute feh."""
    feh_header = [
        '/usr/bin/env feh',
        '--randomize',
        '--bg-scale',
        '--quiet', '--no-menus',
        ]
    fehcmd = []
    fehcmd.extend(feh_header)
    fehcmd.append(currentThemeBG + '/*')
    return(fehcmd)


def currentBg():
    """Read the newly written fehbg to get the file selected as bg."""
    with open(currentThemeBG + '/.fehbg', 'r') as fehbg:
        for line in fehbg.read().split():
            if home in line:
                bgLoc = line.replace("'", "")
                return(bgLoc)
# End of setting feh scripts


# Start reading the background image to get our output colors
def colorList(img):
    """Make a list of the rgb values of all the pixels"""
    width, height = img.size
    rgbcolors = []
    for x in range(width):
        for y in range(height):
            r, g, b = img.getpixel((x, y))
            rgbcolors.append([r, g, b])
        return rgbcolors

def hslSort(rgbcolors):
    """Sort colorvalues by HSL."""
    hslcolors = rgbcolors.sort(key=lambda rgb: colorsys.rgb_to_hsv(*rgb))
    return hslcolors


def rgbToHex(r, g, b):
    """Convert rgb output values to hex values."""
    return '#%02x%02x%02x' % (r, g, b)


def makeHexDict(rgbcolor):
    """Read the image and populate the dictionary with unique hexvalues."""
    hexvalue = rgbToHex(rgbcolor[0], rgbcolor[1], rgbcolor[2])
    if hexvalue not in hexdict:
       hexdict[hexvalue] = int(0)
    hexdict[hexvalue] += 1
    return hexdict
# End creating the color dictionary 


# Pave the way to change the conkyrc color values
def conkyDefault():
    """Read the conky conf for this Hour and set the background color."""
    with open(currentThemeConf + '/conky/datetime.conf', 'r') as conkyrc:
        for line in conkyrc:
            if 'default_color' in line:
                conkyDefaultColor = line.rstrip('\n')
                return(conkyDefaultColor)

def conkyWindow():
    """Read the conky conf for this Hour and set the background color."""
    with open(currentThemeConf + '/conky/datetime.conf', 'r') as conkyrc:
        for line in conkyrc:
            if 'own_window_colour' in line:
                conkyWindowColor = line.rstrip('\n')
                return(conkyWindowColor)
# End returning the conky color values
