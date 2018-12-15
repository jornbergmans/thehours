#!/usr/bin/env python3
"""Read through an image and return the 16 most dominant color values."""

import re
from generators import get

# Set theme to the current hour
currentTheme = get.bgHour()
# End setting the theme


# The feh function for setting the backgrond we will use for the rest.
def fehBg(bgLoc):
    """Build up the string to execute feh."""
    feh_header = [
        '/usr/bin/env', 'feh',
        '--bg-scale',
        '--quiet', '--no-menus',
        '--no-fehbg',
        ]
    fehcmd = []
    fehcmd.extend(feh_header)
    fehcmd.append(bgLoc[1])
    fehcmd.append(bgLoc[2])
    return(fehcmd)
# End setting background images via feh


# Function and info used for getting / setting conkyrc color values
reghex = re.compile('#[a-z0-9]*')


def conkyDefault(hexlist):
    """Read the conky conf for this Hour and set the background color."""
    with open(get.home + '/.themes/thehours/config/conky/datetime.conf', 'r') as conkyrc_input:
        with open(get.home + '/.config/conky/datetime.conf', 'w') as conkyrc_output:
            for line in conkyrc_input:
                if 'default_color' in line:
                    conkyDefaultColor = line
                    conkyNewDefault = re.sub(reghex, hexlist[15],
                                             conkyDefaultColor, 1)
                    conkyrc_output.write(conkyNewDefault)
                else:
                    conkyrc_output.write(line)
                if 'own_window_colour' in line:
                    conkyWindowColor = line
                    conkyNewWindow = re.sub(reghex, hexlist[7],
                                            conkyWindowColor, 1)
                    conkyrc_output.write(conkyNewWindow)
# End setting the conky color values
