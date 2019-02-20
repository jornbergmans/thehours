#!/usr/bin/env python3
"""Read through an image and return the 16 most dominant color values."""

import re
from generators import get

# Set theme to the current hour
currentTheme = get.currentTheme
currentThemeConfigPath = str(get.home + '/.themes/thehours/config/' + currentTheme + '/')
# End setting the theme


# The feh function for setting the background we will use
def fehBg(bgLoc):
    """Build up the string to execute feh."""
    feh_header = [
        'feh',
        '--bg-scale',
        '--quiet', '--no-menus',
        '--no-fehbg',
        ]
    fehcmd = []
    fehcmd.extend(feh_header)
    fehcmd.append(bgLoc[0])
    fehcmd.append(bgLoc[1])
    return(fehcmd)
# End setting background images via feh


# Function and info used for getting / setting conkyrc color values
reghex = re.compile('#[a-z0-9]*')
allHexValues = ['#000000', '#111111', '#222222', '#333333',
                '#444444', '#555555', '#666666', '#777777',
                '#888888', '#999999', '#aaaaaa', '#bbbbbb',
                '#cccccc', '#dddddd', '#eeeeee', '#ffffff']


def conkyColors(hexlist):
    """Read the conky conf for this Hour and set the background color."""
    with open(get.home + '/.themes/thehours/config/default/conky/datetime.conf', 'r') as conkyrc_input:
        with open(currentThemeConfigPath + 'conky/datetime.conf', 'w') as conkyrc_output:
            for line in conkyrc_input:
                conkyNewColor = line
                for hexValue in allHexValues:
                    hexValueIndex = allHexValues.index(hexValue)
                    if hexValue in line:
                        conkyNewColor = conkyNewColor.replace(hexValue, hexlist[hexValueIndex])
                conkyrc_output.write(conkyNewColor)
# End setting the conky color values


def gtkColors(hexlist):
    """Read the gtk base file, and write the new colors for this Hour to the right places."""
    with open(get.home + '/.themes/thehours/config/default/gtk-2.0/gtkrc', 'r') as gtk_input:
        with open(currentThemeConfigPath + 'gtk-2.0/gtkrc', 'w') as gtk_output:
            for line in gtk_input:
                gtkNewColor = line
                for hexValue in allHexValues:
                    hexValueIndex = allHexValues.index(hexValue)
                    if hexValue in line:
                        gtkNewColor = gtkNewColor.replace(hexValue, hexlist[hexValueIndex])
                gtk_output.write(gtkNewColor)
# End setting new gtk color theme


def obColors(hexlist):
    """Read the gtk base file, and write the new colors for this Hour to the right places."""
    with open(get.home + '/.themes/thehours/config/default/openbox-3/themerc', 'r') as ob_input:
        with open(currentThemeConfigPath + 'openbox-3/themerc', 'w') as ob_output:
            for line in ob_input:
                obNewColor = line
                for hexValue in allHexValues:
                    hexValueIndex = allHexValues.index(hexValue)
                    if hexValue in line:
                        obNewColor = obNewColor.replace(hexValue, hexlist[hexValueIndex])
                ob_output.write(obNewColor)
