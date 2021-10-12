#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os

from numpy import array
from pylab import *
from PIL import Image


# convert 参数主要选项: "L", "1"
# camp 参数主要选项: "plt.cm.hot"(热力图)
# clabel参数为是否标注等高线数值
def footprint_recognition(image_file, convert="L", camp=None, clabel=True):
    gray = Image.open(image_file).convert(convert)
    img = array(gray)
    contour = plt.contour(img, 3, colors='black', linewidths=0.5)
    if camp:
        contour = plt.contour(img, 5, cmap=camp)
    if clabel:
        plt.clabel(contour, fontsize=10, colors=('k', 'r'))
    plt.axis('off')
    save_file = os.path.join("result", os.path.basename(image_file))
    if not os.path.exists("result"):
        os.mkdir("result")
    plt.savefig(save_file)


def main():
    input_dir = "image_input"
    images = [os.path.join(input_dir, i) for i in os.listdir(input_dir)]
    for image_file in images:
        footprint_recognition(image_file, convert="L", camp=plt.cm.hot, clabel=False)
        # footprint_recognition(image_file, convert="L", camp=None, clabel=False)


if __name__ == '__main__':
    main()
