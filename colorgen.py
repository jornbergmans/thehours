#!/usr/bin/env python3

import os
import sys
from PIL import Image

_imgLocation = sys.argv[1]
_imgFolder = os.path.split(_imgLocation)[0]

_img = Image.open(_imgLocation)
_imgConverted = _img.convert('RGB')

def rgb_to_hex(r, g, b):
    return '#%02x%02x%02x' % (r, g, b)

width, height = _img.size
outlog = os.path.join(
    _imgFolder,
    "{}.{}".format(
        os.path.splitext(_imgLocation)[0],
        'txt'
    ))

hexdict = {}

if __name__ == "__main__":

	for x in range(width):
		for y in range(height):
			r, g, b = _imgConverted.getpixel((x, y))
			hexvalue = (rgb_to_hex(r, g, b))
			if hexvalue not in hexdict:
				hexdict[hexvalue] = int(0)
			hexdict[hexvalue] += 1
	hexlist = sorted(hexdict, key=hexdict.get, reverse=True)
	print(hexlist[:16])
#	print(hexdict)
