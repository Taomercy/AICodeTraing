#!/usr/bin/env python
# -*- coding:utf-8 -*-
from scipy.special import gamma as Gamma
#from scitools.std import *
from pylab import *


def f1(x):
    return Gamma(x)


def main():
    x = linspace(-6, 6, 512)
    y1 = f1(x)
    gca().set_autoscale_on(False)

    # Matlab-style syntax:
    plot(x, y1)

    xlabel('x')
    ylabel('y')
    # legend(r'$\Gamma(x)$')
    axis([-6, 6, -100, 100])
    grid(True)

    show()


if __name__ == '__main__':
    main()

