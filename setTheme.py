#!/usr/bin/env python3
"""Select background and schemes appropriate to the Hour."""

import subprocess as sp
import sys
sys.path.insert(0, './generators/')
from hourcheck import _bgHour

_bgHourDir = ''

feh_header = [
    '/usr/bin/env feh',
    '--randomize',
    '--no-fehbg',
    '--bg-scale'
    ]


if __name__ == "__main__":

    _bgHourDir = _bgHour(_bgHourDir)

    print(_bgHourDir)

    feh_cmd = []
    feh_cmd.extend(feh_header)
    feh_cmd.append('~/.themes/theHours/wallpapers/' + _bgHourDir + '/*')

    print(feh_cmd)
