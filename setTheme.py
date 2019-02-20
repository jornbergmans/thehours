#!/usr/bin/env python3


import subprocess as sp
from shutil import copyfile
from generators import get
from generators import set
import getTheme

# Set the requested theme to work with
currentTheme = get.currentTheme
currentThemeConfigPath = set.currentThemeConfigPath
conkyThemePath = str(set.currentThemeConfigPath + 'conky/datetime.conf')
gtkThemePath = str(set.currentThemeConfigPath + 'gtk-2.0/gtkrc')
obThemePath = str(set.currentThemeConfigPath + 'openbox-3/themerc')
fehThemePath = str(set.currentThemeConfigPath + 'feh/.fehbg')
# End setting directories for working theme

# Set locations for live files
conkyLivePath = str(get.home + '/.config/conky/datetime.conf')
gtkLivePath = str(get.home + '/.themes/thehours/gtk-2.0/gtkrc')
obLivePath = str(get.home + '/.themes/thehours/openbox-3/themerc')
fehLivePath = str(get.home + '/.fehbg')

# Running these will write an output,
# and copy the respective outputs to the live file
copyfile(conkyThemePath, conkyLivePath)
copyfile(gtkThemePath, gtkLivePath)
copyfile(obThemePath, obLivePath)
copyfile(fehThemePath, fehLivePath)
sp.run(fehLivePath)
