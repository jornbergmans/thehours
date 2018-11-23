#!/usr/bin/env python3
"""Select background and schemes appropriate to the Hour."""

import subprocess as sp
import os
from generators import hourcheck

theHourTheme = ''
home = os.path.expanduser('~')
currentTheme = hourcheck.bgHour(theHourTheme)
currentThemeBG = str(home + '/.themes/thehours/backgrounds/' + currentTheme)

feh_header = [
    '/usr/bin/env feh',
    '--randomize',
    '--bg-scale',
    '--quiet', '--no-menus',
    ]

feh_cmd = []
feh_cmd.extend(feh_header)
feh_cmd.append(currentThemeBG + '/*')

sp.run(feh_cmd)
os.rename(home + '/.fehbg', currentThemeBG + '/.fehbg')

def currentBg():
    """Read the newly written fehbg to get the file selected as bg."""
    with open(currentThemeBG + '/.fehbg', 'r') as fehbg:
        for line in fehbg.read().split():
            if home in line:
                line = line.replace("'", "")
                return(line)

