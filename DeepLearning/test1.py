#!/usr/bin/env python
# -*- coding:utf-8 -*-
from __future__ import division
import numpy as np


def AND(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7
    total = x1 * w1 + x2 * w2
    #print "total:", total
    if total > theta:
        return 1
    else:
        return 0

