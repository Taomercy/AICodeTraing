#!/usr/bin/env python
# -*- coding:utf-8 -*-
from pylab import *
from PIL import Image

image_name = "footprint1.jpg"
# image_name = "footprint.jpg"
gray = Image.open(image_name).convert('1')
# gray = Image.open(image_name).convert('L')
plt.imshow(gray, cmap=plt.cm.gray_r)
plt.axis('off')
plt.show()


img = array(gray)
# contour = plt.contour(img, 3, colors='black', linewidths=0.5)
contour = plt.contour(img, 5, cmap=plt.cm.hot)
# plt.clabel(contour, fontsize=10, colors=('k', 'r'))
plt.axis('off')
plt.show()
