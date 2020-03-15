#!/usr/bin/env python
# -*- coding:utf-8 -*-
from __future__ import division
import numpy as np
# 人为定制权重参数， 编写神经网络


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def init_network():
    network = {}
    network['W1'] = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
    network['b1'] = np.array([0.1, 0.2, 0.3])

    network['W2'] = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
    network['b2'] = np.array([0.1, 0.2])

    network['W3'] = np.array([[0.1, 0.3], [0.2, 0.4]])
    network['b3'] = np.array([0.1, 0.2])

    return network


# 输出层激活函数
def identity_function(x):
    return x


def forward(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    # 第一层
    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)

    # 第二层
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)

    # 第三层
    a3 = np.dot(z2, W3) + b3
    z3 = identity_function(a3)

    return z3


def main():
    network = init_network()
    x = np.array([1.0, 0.5])
    y = forward(network, x)
    print(y)


if __name__ == '__main__':
    main()















