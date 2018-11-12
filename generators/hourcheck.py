#!/usr/bin/env python3
"""Check the time and return the theme we will use for this Hour."""

import datetime
theHour = int(datetime.datetime.now().strftime('%H'))


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
# end checking Hour
