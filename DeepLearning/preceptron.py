#!/usr/bin/env python
# -*- coding:utf-8 -*-
from __future__ import division
import numpy as np


def AND(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7
    total = x1 * w1 + x2 * w2
    # print("total:", total)
    if total > theta:
        return 1
    else:
        return 0


def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1


def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1


def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)
    return y


