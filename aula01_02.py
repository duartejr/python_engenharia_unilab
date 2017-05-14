#-*- coding: utf-8 -*-
#trabalhando com vetores

import numpy as np
a = np.array([0,1,2])
print a.shape
print a
#Transposta
print a.T

#produto escalar
print np.dot(a, a) 
print np.dot(a, a.T)

b = np.array([[0,1,2]])
print b.shape
print b
print b.T

print np.dot(b, b.T)

x = np.array([[2],[4],[6],[8]])
y = np.array([1,1,1,1,1,2])
print x
print y
print x+y

#Resolvendo equações lineares
A = np.array([[1,  -1,   1],
			  [0,  10,  25],
			  [20, 10,   0]])

b = np.array([0,90,80])

x = np.linalg.solve(A, b)
print x
print np.dot(A, x)

print np.dot(A, x) == b

#matriz transposta
import numpy as np
A = np.array([[5,8,1],
	          [4,0,0]])
print np.transpose(A)
print A.T

#somatório
a = np.array([1,2,3,4,5])
b = np.array([3,6,8,9,10])
print np.sum(a*b)

w = np.array([0.1,.25,.12,.45,.98])
v = np.array([9,7,11,12,8])
y = np.sum(w * v**2)
print y

#Determinante
from scipy.linalg import lu

A = np.array([[6,2,3],
	          [1,1,1],
	          [0,4,9]])

print np.linalg.det(A)