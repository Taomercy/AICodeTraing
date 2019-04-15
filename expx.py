#!/usr/bin/env python
# -*- coding:utf-8 -*-
#!/usr/bin/env python
# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np


def expx(x):
    y = np.ones_like(x)
    i = x > 0
    y[i] = np.power(x[i], x[i])
    i = x < 0
    y[i] = np.power(-x[i], -x[i])
    return y


def expx_main():
    x = np.linspace(-1.5, 2, 1000)
    y = expx(x)
    plt.plot(x, y, 'b-', label='x^x', linewidth=2)
    plt.grid(True)
    plt.legend(loc='upper left')
    plt.show()


def lnx(x):
    return np.log(x)


def lnx_main():
    x = np.linspace(0, 5, 1000)
    y = lnx(x)
    plt.plot(x, y, 'b-', label='lnx', linewidth=2)
    plt.grid(True)
    plt.legend(loc='upper left')
    plt.show()


if __name__ == '__main__':
    lnx_main()
    expx_main()
