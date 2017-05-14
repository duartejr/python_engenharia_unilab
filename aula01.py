# -*- coding: utf-8 -*-
#Aula01 parte 2
#Operações básicas: aritmética e trigonometria

#soma, subtração, multiplicação e divisão
#soma
print 2+2
a = 1
b = 3
print a+b
a = float(raw_input('a = '))
b = float(raw_input('b = '))
c = a+b
print c

#subtração
print a - b

#divisão
print 4/2
print 4/3
print 4/3.
a = 4
b = 2.
print a/b
a = float(raw_input('a = '))
b = float(raw_input('b = '))

#multiplicação
print 2*2
print 2*2.

#potência
import math
#elevar um número ao quadrado
print a**2
print math.pow(x, y)

#Raiz
print a**(1/2.)
print math.sqrt(a)
y = 1/3. #para raiz cubica
print math.pow(x, y) #y = 1/3. para raiz cubica

#trigonometria
print math.sin(x)
print math.cos(x)
print math.tan(x)
print math.acos(x)

#Aula01 parte 3
#Estatística básica
#Média
import numpy as np
A = np.array([1,2,3,4,5])
B = np.array([1,4,5,6,7])
print np.mean(A)
print np.std(A)
print np.median(A)
print np.min(A)
print np.max(A)
print np.var(A)
print np.corrcoef(A,B)
from scipy.stats import mode
print mode(A)[0][0]

#Aula 01 parte 4
#Resolução de sistema de equações lineares