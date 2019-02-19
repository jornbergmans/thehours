#!/usr/bin/env python3

import os
import sys
import subprocess as sp
from shutil import copyfile
from generators import get
from generators import set

# Set the requested theme to work with
if sys.argv[1] in ['dusk', 'day', 'dawn', 'dark']:
    currentTheme = sys.argv[1]
else:
    currentTheme = get.bgHour()

currentThemePath = set.currentThemePath
conkyThemePath = str(currentThemePath + '/conky/datetime.conf')
gtkThemePath = str(currentThemePath + '/gtk-2.0/gtkrc')
# End setting directories for working theme

# Set locations for live files
conkyLivePath = str(get.home + '/.conky/datetime.conf')
gtkLivePath = str(get.home + '/.themes/thehours/gtk-2.0/gtkrc')

print(currentTheme)
print(currentThemePath)
print(conkyThemePath)
print(gtkThemePath)
print(conkyLivePath)
print(gtkLivePath)

set.conkyColors
copyfile(conkyThemePath, conkyLivePath)
sp.run('/usr/bin/env', 'conky', '-c', conkyLivePath)

set.gtkColors
copyfile(gtkThemePath, gtkLivePath)
sp.run('/usr/bin/env', 'conky', '-c', conkyLivePath)