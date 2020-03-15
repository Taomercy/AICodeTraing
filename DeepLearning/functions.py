#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 使用中心差分求导
from __future__ import division
import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a - c)
    exp_sum = np.sum(exp_a)
    return exp_a / exp_sum


# 交叉熵误差
def cross_entropy_error(y, t):
    if y.ndim == 1:
        t = y.reshape(1, t.size)
        y = y.reshape(1, y.size)
    batch_size = y.shape[0]
    return -np.sum(t * np.log(y + 1e-7)) / batch_size


# 使用中心差分求导
def numerical_gradient(f, x):
    h = 1e-4
    # 生成和x一样维度的数组
    grad = np.zeros_like(x, dtype='float64')

    for idx in range(x.size):
        # grad = (f(x+h) - f(x-h)) / 2*h
        deltx1 = x[idx] + h
        deltx2 = x[idx] - h

        fxh1 = f(deltx1)
        fxh2 = f(deltx2)

        grad[idx] = (fxh1 - fxh2)/(2*h)

    return grad


# init_x 为初始点
def gradient_descent(f, init_x, lr=0.01, step_num=100):
    x = init_x
    for i in range(step_num):
        grad = numerical_gradient(f, init_x)
        x = x - grad * lr
    return x
