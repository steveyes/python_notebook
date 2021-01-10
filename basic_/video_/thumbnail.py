#!/usr/bin/env python3
#

# import from sys
import cv2
from pathlib import Path
from pprint import pprint
from matplotlib import pyplot
import math
import numpy

# import from dist


# import from chekawa


# configs


# constants


# variables


# functions


# instances

if __name__ == '__main__':
    _WIDTH = 640
    _HEIGHT = 480

    video_bytes = open('01.avi', 'rb').read()
    video_numpy = numpy.asarray(bytearray(video_bytes), dtype=numpy.uint8)
    # video_numpy = numpy.fromstring(video_bytes, dtype=numpy.uint8)
    print(type(video_bytes))
    print(video_numpy)

    cap = cv2.VideoCapture(video_numpy, cv2.IMREAD_COLOR)


    # fps
    fps = cap.get(cv2.CAP_PROP_FPS)

    # 宽，高
    width, height = (cap.get(cv2.CAP_PROP_FRAME_WIDTH), cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # 视频帧总数
    frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)

    pprint(fps)
    pprint(width)
    pprint(height)
    pprint(frame_count)

    # 计算视频总时长
    duration = math.floor(frame_count / fps)
    pprint(duration)

    # 截获一秒的最后一帧
    cap.set(cv2.CAP_PROP_POS_FRAMES, fps)
    success, frame = cap.read()

    # 计算缩放比例
    if width > _WIDTH:
        _RATIO = width / _WIDTH
    elif height > _HEIGHT:
        _RATIO = height / _HEIGHT
    else:
        _RATIO = 1

    # 缩放
    width_resized = round(width / _RATIO)
    height_resized = round(height / _RATIO)
    img = cv2.resize(frame, (width_resized, height_resized))

    # 显示图片
    pyplot.imshow(img)
    pyplot.show()

    # 保存图片
    cv2.imwrite('123.jpg', img=img)

    cap.release()
