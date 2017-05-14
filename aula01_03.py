# -*- coding: utf-8 -*-
'''Resolver o sistema de equações
2+x+y-x²+8xy+y³=0
1+2x-3y+x²+xy-ye^x=0
'''
import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

def f(x,y):
	return 2 + x + y - x**2 + 8*x*y + y**3

def g(x,y):
	return 1 + 2*x - 3*y + x**2 - x*y - y*np.exp(x)

x = np.linspace(-5, 5, 500)

@np.vectorize
def fy(x):
	x0 = 0.0
	def tmp(y):
		return f(x, y)
	y1, = fsolve(tmp, x0)
	return y1

@np.vectorize
def gy(x):
	x0 = 0.0
	def tmp(y):
		return g(x, y)
	y1, = fsolve(tmp, x0)
	return y1

plt.plot(x,fy(x),x,gy(x))
plt.ylabel('y')
plt.xlabel('x')
plt.legend(['fy','gy'])
plt.show()	

def func(X):
	x,y = X
	return [f(x,y),g(x,y)]
print fsolve(func, [-2,-2])