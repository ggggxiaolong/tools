#!/usr/bin/python
# -*- coding: utf-8 -*-

import os.path
import sys
from PIL import Image

"""
将Png图片转换为Jpg格式
"""

def convert(dir):
    im = Image.open(dir)
    res = im.convert('RGB')
    res.save(os.path.splitext(dir)[0] + ".jpg")

if __name__ == "__main__":
    if sys.argv[1]:
        convert(sys.argv[1])