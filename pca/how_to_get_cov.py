from __future__ import division
import numpy as np
A = np.matrix([[1,2,3], [5,4,1], [1, 4, 2]])
X = np.matrix(A)
arv = np.mean(A, axis=0)
m, n = np.shape(A)
agvs = np.tile(arv, (m, 1))
print "A=\n", A
print "agvs=\n", agvs
X1 = X-np.matrix(agvs)
print "X1=\n", X1
print np.dot(X1.T, X1)*(1/(m-1))

print "========="
print np.cov(A.T)


