#!/usr/bin/env python
# -*- coding:utf-8 -*-
from pylab import *
from PIL import Image

image_name = "footprint.jpg"
gray = Image.open(image_name).convert('1')
plt.imshow(gray, cmap=plt.cm.gray_r)
plt.axis('off')
plt.show()


img = array(gray)
print(img)
contour = plt.contour(img, 3, colors='black', linewidths=0.5)
plt.clabel(contour, fontsize=10, colors=('k', 'r'))
plt.axis('off')
plt.show()
