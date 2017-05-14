# -*- coding: utf-8 -*-
"""
Exemplo simples de gráfico de linhas
"""
import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0, 10, 500)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x,y1,'--',linewidth=2,color='k',label='sin(X)')
plt.plot(x,y2,'-.',linewidth=2,color='r',label='cos(x)')
plt.grid()
plt.xlabel(u'Ângulo (rad)',fontsize=14)
plt.ylabel('y',fontsize=14)
plt.legend(loc='upper left')
plt.title(u'Exemplo gráfico de linhas', fontsize=22, color='b')
plt.xticks(range(0,11,1))
plt.yticks(np.arange(-1,1.1,.25))
plt.show()