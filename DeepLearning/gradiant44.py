#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 求函数f(x0, x1)= x0**2 + x1**2 的最小梯度
from __future__ import division
import numpy as np


def function_model(x):
    return np.sum(x**2)
    # return x[0]**2 + x[1]**2


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
        #x = x - grad * lr
        x[0] -= grad[0] * lr
        x[1] -= grad[1] * lr
        print(x)
    return x


def main():
    init_x = np.array([-3, 4])
    grad = gradient_descent(function_model, init_x)
    print(grad)


if __name__ == '__main__':
    main()
