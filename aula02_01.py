#-*- coding: utf-8 -*-

from sympy import Symbol

x = Symbol('x')
y = Symbol('y')

print 2 * x - x

print x + y + x + 10 * y

print (x + y)**2

import sympy

x,y,z = sympy.symbols('x,y,z')

print x + 2*y + 3*z - x


from sympy import symbols

x, y = symbols('x,y')

print x + 2*y

print (x + 2*y).subs(x, 2)

print (x + 2*y).subs(y, 10)

print (x + 2*y).subs(x, 2).subs(y,10)

print (x + 2*y).subs({x:2,y:10})

myterm = x + 2*y

print myterm

print myterm.subs({x:2,y:10})

from sympy import *

a = Rational(1,10)
b = Rational(45,67)
print a
print b
print a*b

from sympy import Symbol, exp, sin, sqrt, diff

x = Symbol('x')
y = Symbol('y')

print diff(sin(x),x)
print diff(10 + 3*x + 4*y + 10*x**2 + x**9,y)
print diff(10 + 3*x + 4*y + 10*x**2 + x**9, x).subs(x,1)
print diff (10 + 3*x + 4*y + 10*x**2 + x**9, x).subs(x ,1.5)
print diff(exp(x), x)
print diff(exp(-x ** 2 / 2), x)
print diff (3*x**4, x, 3)
print diff (3*x**4*y**7, x, 2, y, 2)
print diff(diff (3*x**4*y**7, x, x), y, y)

r = sqrt(x**2 + y**2)
sigma = Symbol('sigma')

def phi(x,y,sigma):
	return sqrt(x**2 + y**2 + sigma**2)

mydfdx= x / sqrt(r**2 + sigma**2)
print diff(phi(x, y, sigma), x)
print mydfdx - diff(phi(x, y, sigma), x)

from sympy import integrate

print integrate(2*x,(x,0,1))
print float(integrate(x**2,(x,0,2)))
print integrate(x**2,x)

from sympy import Symbol, dsolve, Function, Derivative, Eq

y = Function("y")
x = Symbol('x')
y_ = Derivative(y(x), x)
print dsolve(y_+5*y(x),y(x))
print dsolve(Eq(y_ + 5*y(x), 0), y(x))
print dsolve(Eq(y_ + 5*y(x), 12), y(x))
z = dsolve(y_ + 5*y(x), y(x))
print
print z
print z.rhs
print
C1 = Symbol('C1')
y3 = z.subs({C1:2,x:3})
print
print y3
print y3.evalf(10)
print y3.rhs