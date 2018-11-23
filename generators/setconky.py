#!/usr/bin/env python3
"""Read colors generated and set conky colorscheme appropriate to the Hour."""

import subprocess as sp
import os
import re
from generators import hourcheck
from generators import colorgen

home = os.path.expanduser('~')
theHourTheme = ''
currentTheme = hourcheck.bgHour(theHourTheme)
currentThemeConf = str(home + '/.themes/thehours/configs/' + currentTheme)

hex1 = colorgen.populate_dictionary()


def conkycolors():
    """Read the conky conf for this Hour and set the background color."""
    with open(currentThemeConf + '/conky/datetime.conf', 'r') as conkyrc:
        hexvalue = re.compile('\#[0-9]*')
        for line in conkyrc.read().split():
            if 'default_color' in line:
                re.sub(hexvalue, 'hex1')
            elif 'own_window_color' in line:
                re.sub(hexvalue, 'hex2')



