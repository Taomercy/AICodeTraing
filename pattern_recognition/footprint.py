#!/usr/bin/env python
# -*- coding:utf-8 -*-
import cv2
import matplotlib.pyplot as plt
image_name = "footprint.jpg"
img = cv2.imread(image_name)
img = img[:, :, (2, 1, 0)]

# 调整通道
r, g, b = [img[:, :, i] for i in range(3)]
img_gray = r * 0.299 + g * 0.587 + b * 0.114

plt.imshow(img_gray, cmap=plt.cm.gray_r)
plt.axis('off')
plt.show()


#!/usr/bin/env python
# -*- coding:utf-8 -*-
from pylab import *
from PIL import Image

image_name = "footprint.jpg"
gray = Image.open(image_name).convert('L')
plt.imshow(gray, cmap=plt.cm.gray_r)
plt.axis('off')
plt.show()
