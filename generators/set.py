#!/usr/bin/env python3
"""Read through an image and return the 16 most dominant color values."""

import subprocess as sp
import os
import sys
import re
from generators import get

### This means that our theme will be set to the current hour, like so
currentTheme = get.bgHour()
bgLoc = get.currentBg()
# End setting the theme
# The feh function for setting the backgrond we will use for the rest.
def fehfunct():
    """Build up the string to execute feh."""
    feh_header = [
        '/usr/bin/env feh',
        '--bg-scale',
        '--quiet', '--no-menus',
        '--no-fehbg',
        ]
    fehcmd = []
    fehcmd.extend(feh_header)
    fehcmd.append(bgLoc)
    return(fehcmd)
# End of feh

# Function and info used for getting / setting conkyrc color values
reghex = re.compile('\#[a-z0-9]*')


def conkyDefault(hexlist):
    """Read the conky conf for this Hour and set the background color."""
    with open(get.currentThemeConf + '/conky/datetime.conf', 'r') as conkyrc_input, open(get.home + '/.config/conky/datetime.conf', 'w') as conkyrc_output:
        for line in conkyrc_input:
            if 'default_color' in line:
                conkyDefaultColor = line.rstrip('\n')
                print("THIS IS THE LINE WE'RE LOOKING FOR " + line)
                print('conkyDefaultColor = ' + str(conkyDefaultColor))
                conkyNewDefault = re.sub(reghex, hexlist[4], conkyDefaultColor, 1)
                print('conkyNewDefault = ' + str(conkyNewDefault))
                print('conkyrc_output.write(' + conkyNewDefault + ')')
#            else:
#                conkyrc_output.write(line)
            if 'own_window_colour' in line:
                conkyWindowColor = line.rstrip('\n')
                print('conkyWindowColor = ' + str(conkyWindowColor))
                conkyNewWindow = re.sub(reghex, hexlist[7], conkyWindowColor, 1)
                print('conkyNewWindow = ' + str(conkyNewWindow))
                print('conkyrc_output.write(' + conkyNewWindow + ')')
#            else:
#                conkyrc_output.write(line)

# End returning the conky color values
