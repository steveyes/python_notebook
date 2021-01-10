#!/usr/bin/env python3
#

# import from sys
from PIL import Image
from matplotlib import pyplot


def compress01(max_width=None, max_height=None):
    img = Image.open('01.png')

    pyplot.imshow(img)
    pyplot.show()
    (width, height) = img.size
    print(width)
    print(height)

    if width > max_width:
        ratio = max_width / width
    elif height > max_height:
        ratio = max_height / height
    else:
        ratio = 1

    print(ratio)

    new_width = int(width * ratio)
    new_height = int(height * ratio)

    new_img = img.resize((new_width, new_height))

    pyplot.imshow(new_img)
    pyplot.show()


if __name__ == '__main__':
    compress01()
