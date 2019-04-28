#!/usr/bin/env python
# -*- coding:utf-8 -*-
from __future__ import division
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression, LassoCV, RidgeCV, ElasticNetCV
from sklearn.pipeline import Pipeline
import warnings
from sklearn.exceptions import ConvergenceWarning
from sklearn.preprocessing import PolynomialFeatures


def xss(y, y_hat):
    y = y.ravel()
    y_hat = y_hat.ravel()
    tss = (y - np.average(y)**2).sum()
    rss = ((y_hat - y)**2).sum()
    ess = ((y_hat - np.average(y))**2).sum()
    r2 = 1 - rss /tss
    tss_list.append(tss)
    rss_list.append(rss)
    ess_list.append(ess)
    ess_rss_list.append(rss + ess)

    corr_coef = np.corrcoef(y, y_hat)[0, 1]
    return r2, corr_coef


if __name__ == '__main__':
    warnings.filterwarnings(action='ignore', category=ConvergenceWarning)
    np.random.seed(0)
    np.set_printoptions(linewidth=300)
    N = 9
    Max = 6
    x = np.linspace(0, Max, N) + np.random.randn(N)
    x.sort()
    y = x**2 + 4*x - 3 + np.random.randn(N)
    x.shape = -1, 1
    y.shape = -1, 1
    
    print "x:", x
    print "y:", y

    models = [
        Pipeline([
            ('poly', PolynomialFeatures()),
            ('linear', LinearRegression(fit_intercept=False))
        ]),
        Pipeline([
            ('poly', PolynomialFeatures()),
            ('linear', RidgeCV(alphas=np.logspace(-3, 2, 50), fit_intercept=False))
        ]),
        Pipeline([
            ('poly', PolynomialFeatures()),
            ('linear', LassoCV(alphas=np.logspace(-3, 2, 50), fit_intercept=False))
        ]),
        Pipeline([
            ('poly', PolynomialFeatures()),
            ('linear', ElasticNetCV(alphas=np.logspace(-3, 2, 50), fit_intercept=False,
                                    l1_ratio=[0.1, 0.5, 0.7, 0.9, 0.95, 0.99, 1]))
        ]),
    ]

    #mpl.rcParams['font.sans-serif'] = [u'SimHei']
    #mpl.rcParams['axes.unicode_minus'] = False
    np.set_printoptions(suppress=True)

    plt.figure(figsize=(18, 12), facecolor='w')
    order_pool = np.arange(1, N, 1)
    m = order_pool.size
    colors = []
    for c in np.linspace(16711680, 225, m):
        colors.append('#%06x' % c)

    line_width = np.linspace(5, 2, m)

    titles = ['Linear', 'Ridge', 'Lasso', 'ElasticNet']
    tss_list = []
    rss_list = []
    ess_list = []
    ess_rss_list = []

    for t in range(4):
        model = models[t]
        plt.subplot(2, 2, t+1)
        plt.plot(x, y, 'ro', ms=10, zorder=N)
        for i, d in enumerate(order_pool):
            model.set_params(poly__degree=d)
            model.fit(x, y.ravel())
            lin = model.get_params('linear')['linear']
            output = u"%s: %d阶系数为：" % (titles[t], d)
            if hasattr(lin, 'alpha_'):
                idx = output.find(u'系数')
                output = output[:idx] + ('alpha=%.6f' % lin.alpha_) + output[idx:]
            if hasattr(lin, 'l1_ratio_'):
                idx = output.find(u'系数')
                output = output[:idx] + ('l1_ratio=%.6f' % lin.l1_ratio_) + output[idx:]
            print output, lin.coef_.ravel()

            x_hat = np.linspace(x.min(), x.max(), num=100)
            x_hat.shape = -1, 1
            y_hat = model.predict(x_hat)
            score = model.score(x, y)
            r2, corr_coef = xss(y, model.predict(x))

            z = N - 1 if (d == 2) else 0
            label = '%d order, R^2=%.3f' % (d, r2)
            if hasattr(lin, 'l1_ratio_'):
                label += ', L1_ratio=%.2f' % lin.l1_ratio_
            plt.plot(x_hat, y_hat, color=colors[i], lw=line_width[i], alpha=0.75, label=label, zorder=z)

        plt.legend(loc='upper left')
        plt.grid(True)
        plt.title(titles[t], fontsize=18)
        plt.xlabel('X', fontsize=16)
        plt.ylabel('Y', fontsize=16)

    plt.tight_layout(1, rect=(0, 0, 1, 0.95))
    plt.suptitle('Comparison of polynomial curve fitting', fontsize=22)
    plt.savefig("Comparison_of_polynomial_curve_fitting.png")
    plt.show()

    y_max = max(max(tss_list), max(ess_rss_list)) * 1.05
    plt.figure(figsize=(9, 7), facecolor='w')
    t = np.arange(len(tss_list))
    plt.plot(t, tss_list, 'ro-', lw=2, label='TSS(Total Sum of Squares)')
    plt.plot(t, ess_list, 'mo-', lw=1, label='ESS(Explained Sum of Squares)')
    plt.plot(t, rss_list, 'bo-', lw=1, label='RSS(Residual Sum of Squares)')
    plt.plot(t, ess_rss_list, 'go-', lw=2, label='ESS+RSS')
    plt.ylim(0, y_max)
    plt.legend(loc='center right')
    plt.xlabel('/Ridge/LASSO/Elastic Net', fontsize=15)
    plt.ylabel('XSS', fontsize=15)
    plt.title('TSS', fontsize=18)
    plt.grid(True)
    plt.savefig("TSS.png")
    plt.show()
    







