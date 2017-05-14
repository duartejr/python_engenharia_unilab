# -*- coding: utf-8 -*-
"""
Exemplo simples de um histograma
"""

import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

np.random.seed(0)

# example data
mu = 100  # mean of distribution
sigma = 15  # standard deviation of distribution
x = mu + sigma * np.random.randn(437)

num_cols = 10

max_x = int(np.ceil(np.max(x)))
min_x = int(np.floor(np.min(x)))
ticks = (max_x-min_x)/float(num_cols)

plt.hist(x,num_cols,range=[min_x,max_x],normed=True,cumulative=True)
plt.xticks(np.arange(min_x,max_x+1,ticks))
plt.grid()
plt.xlabel(u'Valores aleatórios')
plt.ylabel(u'Frequência (%)')
plt.title('Exemplo de histograma')
plt.xlim(min_x,max_x)
plt.yticks(np.arange(0,1.1,.10),np.arange(0,1.1,.1)*100)
plt.ylim(0,1.0)
plt.show()