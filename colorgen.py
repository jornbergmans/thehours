#!/usr/bin/env python3

import os
import sys
from PIL import Image
#

imageFolder = sys.argv[1]

def rgb_to_hex(r, g, b):
    return '#%02x%02x%02x' % (r, g, b)

_theImageLocation = '/Users/vtr/Downloads/wallpapers/inputfiles/dawn/palettes/highlands_castle_by_kvacm-dbzuyr8-palette.png'
_theImage = Image.open(_theImageLocation)

pixels = _theImage.convert('RGB')
width, height = _theImage.size
outlog = os.path.join(
    imageFolder,
    "{}.{}".format(
        os.path.splitext(_theImageLocation)[0],
        'txt'
    ))

outlist = []

for x in range(width):
	for y in range(height):
		r, g, b = pixels.getpixel((x, y))
		print(rgb_to_hex(r, g, b))
#		logfile = open(outlog, 'a')
#		logfile.write(rgb_to_hex(r, g, b))
#		logfile.write(' ')
		outlist.append(rgb_to_hex(r, g, b))
print(outlist)
