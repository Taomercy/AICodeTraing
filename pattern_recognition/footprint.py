#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os

import cv2
import matplotlib.pyplot as plt
directory = "image_input"
image_name = os.path.join(directory, "footprint_low.jpg")
img = cv2.imread(image_name)
img = img[:, :, (2, 1, 0)]

# 调整通道
r, g, b = [img[:, :, i] for i in range(3)]
img_gray = r * 0.299 + g * 0.587 + b * 0.114

plt.imshow(img_gray, cmap=plt.cm.gray_r)
plt.axis('off')
plt.show()


# method2
from pylab import *
from PIL import Image

gray = Image.open(image_name).convert('L')
plt.imshow(gray, cmap=plt.cm.gray_r)
plt.axis('off')
plt.show()
