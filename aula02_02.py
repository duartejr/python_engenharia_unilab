# -*- coding: utf-8 -*-

#integração numérica
#Regra do trapézio
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division

def trapezio(n,a,b,f):
	'''
	trapezio(n,a,b,f): integra f entre a e b com n trapézios
	'''
	deltax = (b-a)/n
	Se = f(a) + f(b) #define Se
	Si = 0.0 # incializa Si
	for k in range(1,n): # Calcula Si
		xk = n + k*deltax
		Si += f(xk)
	I = Se + 2*Si # cálculo de I
	I *= deltax
	I /= 2
	return I

def f(x):
	return ((-1/48.*x**4 + (13/48.)*x**3 + (-17/12.)*x**2 + (11/3.)*x))

I3 = trapezio(8, 1, 5, f)

print('I3 = %8.4f\n' % I3)

def trapepsilon (epsilon ,a,b,f):
	'''
	trapepsilon (epsilon ,a,b,f): calcula a integral de f entre a e b com
	erro absoluto epsilon , de forma eficiente
	'''
	eps = 2* epsilon
	# estabelece um erro inicial grande
	n = 1
	# n é o número de trapézios
	Se = f(a) + f(b)
	# Se não muda
	deltax = (b-a)/n
	# primeiro deltax
	dx2 = deltax /2
	# primeiro deltax /2
	Siv = 0.0
	# Si " velho "
	Iv = Se*dx2
	# I " velho "
	# executa o loop pelo menos uma vez
	while eps > epsilon :
		Sin = 0.0
		# Si "novo"
		n *= 2
		# dobra o número de trapézios
		deltax /= 2
		# divide deltax por dois
		dx2 = deltax /2
		# idem para dx2
		for i in range (1, n ,2):
			# apenas os ímpares ...
			xi = a + i* deltax
			# pula os ptos já calculados !
			Sin += f(xi)
			# soma sobre os novos ptos internos
		Sin = Sin + Siv
		# aproveita todos os ptos já calculados
		In = (Se + 2* Sin )* dx2
		# I "novo"
		eps = abs(In - Iv)
		# calcula o erro absoluto
		Siv = Sin
		# atualiza Siv
		Iv = In
		# atualiza Iv
	return (In ,eps)

(I5 ,eps) = trapepsilon (0.000001 ,1 ,5 ,f)
print('I5 = %12.7f eps = %12.7f' % (I5 ,eps ))
II = 14.677777777777777
delta = (I5 - II )/ II
print('delta = %12.8f' % delta )
