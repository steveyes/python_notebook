#!/usr/bin/env python3
#




import tesserocr
from PIL import Image


def to_text_chi_sim(im):
    print(tesserocr.image_to_text(im, lang='chi_sim'))


def to_text_bod(im):
    print(tesserocr.image_to_text(im, lang='bod'))

if __name__ == '__main__':
    print(tesserocr.get_languages())
    print(tesserocr.tesseract_version())
    im = Image.open('image_bod.jpg')
    print(to_text_bod(im))

