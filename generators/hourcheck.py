#!/usr/bin/env python3
"""Check the time and return the theme we will use for this Hour."""

import datetime
_theHour = int(datetime.datetime.now().strftime('%H'))


def _bgHour(_bgHourDir):
    """Return the path to the correct wallpaper folder."""
    if 0 <= _theHour <= 6:
        _bgHourDir = 'dark'
    if 6 <= _theHour <= 12:
        _bgHourDir = 'dawn'
    if 12 <= _theHour <= 18:
        _bgHourDir = 'day'
    if 18 <= _theHour <= 23:
        _bgHourDir = 'dusk'
    return _bgHourDir
# end checking Hour
