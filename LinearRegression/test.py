#!/usr/bin/env python
# -*- coding:utf-8 -*-
from numpy import *
import matplotlib.pylab as plt
import sympy
data = array([
    [1.2, 3.6],
    [2.3, 4.6],
    [1.8, 7.6],
    [5.4, 15.8],
])


def plotting(res):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(array(data[:, 0]), array(data[:, 1]))
    x = arange(0, 10, 0.01)
    y = curve(x, res[k], res[b])
    ax.plot(x, y, 'r')
    plt.show()


def curve(x, k, b):
    return k*x + b

# first way
# set y = kx + b
k = sympy.Symbol('k')
b = sympy.Symbol('b')
loss = sympy.Symbol('loss')
for i in data:
    loss += (i[1] - (k*i[0] + b))**2

dlossdk = sympy.diff(loss, k)
dlossdb = sympy.diff(loss, b)

print("dlossdk:", dlossdk)
print("dlossdb:", dlossdb)

res = sympy.solve([dlossdk, dlossdb], [k, b])
plotting(res)
# second way

