# -*- coding: utf-8 -*-
'''
Trabalho - Potencial Eólico
Descrição:
Em anexo segue uma série histórica de 2016 de velocidade do vento referente à estação meteorológica de Guaramiranga,
fornecido pelo Instituto Nacional de Meteorologia - INMET. De acordo com normas internacionais, a altura do anemômetro está
situada a 10 metros da superfície.
'''
import numpy as np
import pandas as pd
from datetime import date
from calendar import monthrange
import matplotlib.pyplot as plt
from scipy import stats

# rho = 1.225 (km/m³) considerando-se T=15ºC e p = 1atm
def pot_eolico(df, anos, alt, X, rho=1.1225):
    print '#######################'
    print '# Resultados para', alt, '#'
    print '#######################'

    meses = {1: 'jan', 2: 'fev', 3: 'mar', 4: 'abr', 5: 'mai', 6: 'jun',
             7: 'jul', 8: 'ago', 9: 'set', 10: 'out', 11: 'nov', 12: 'dez'}

    # velocidade média mensal e anual
    v_mensal = []
    for ano in anos:
        for mes in range(1, 13):
            start = '{0:%d}/{0:%m}/{0:%Y}'.format(date(ano, mes, 01))
            end = '{0:%d}/{0:%m}/{0:%Y}'.format(
                date(ano, mes, monthrange(ano, mes)[1]))
            v_mensal.append(df.ix[start:end].velocidade.mean(0))
    v_mensal = np.reshape(v_mensal, (len(v_mensal)/12, 12))
    std_med_mensal = np.std(v_mensal, 0)
    v_med_mensal = np.mean(v_mensal, 0)
    v_med_anual = np.mean(v_med_mensal)

    print 'Velocidade média mensal: '
    for i in range(len(v_med_mensal)):
        print '{0}:\t{1:.3f} m/s'.format(meses[i+1], v_med_mensal[i])
    print 'Velocidade média anual = {0:.3f} m/s\n'.format(v_med_anual)

    # Gráfico da velocidade anual (por mês)
    plt.plot(range(12), v_med_mensal)
    plt.xticks(range(12), meses.values(), fontsize=12)
    plt.grid()
    plt.xlim([0, 11])
    plt.ylim([0, np.ceil(np.max(v_med_mensal))])
    plt.ylabel('Velocidade (m/s)', fontsize=14)
    plt.title(u'Velocidade média mensal {0}'.format(alt), fontsize=18)
    plt.savefig('velocidade_media_mensal_{0}.png'.format(alt))

    # Desvio padrão mensal e anual;
    std_anual = np.std(v_med_mensal)
    print 'Desvio padrão mensal:'
    for i in range(len(std_med_mensal)):
        print '{0}:\t{1:.3f} m/s'.format(meses[i+1], std_med_mensal[i])
    print 'Desvio padrão anual = {0:.3f} m/s\n'.format(std_anual)
    plt.plot(range(12),v_med_mensal+std_med_mensal)
    plt.plot(range(12),v_med_mensal-std_med_mensal)
    plt.ylim([0, np.ceil(np.max(v_med_mensal+std_med_mensal))])
    plt.legend([u'Valores médios'])
    plt.savefig('velocidade_media_mensal_{0}_std.png'.format(alt))
    plt.close()

    # Densidade de potência mensal e anual;
    dens_pot_mensal = 0.5*rho*np.power(v_med_mensal, 3)
    dens_pot_anual = 0.5*rho*np.power(v_med_anual, 3)

    print 'Densidade de potência média mensal:'
    for i in range(len(dens_pot_mensal)):
        print '{0}:\t{1:.3f} W/m²'.format(meses[i+1], dens_pot_mensal[i])
    print 'Densidade de potência média anual: %.3f W/m²' % (dens_pot_anual)
    
    max_pot_m = np.ceil(np.max(dens_pot_mensal))
    plt.plot(range(12),dens_pot_mensal)
    plt.grid()
    plt.xticks(range(12), meses.values(), fontsize=12)
    plt.xlim(0,11)
    plt.ylim([0, max_pot_m])
    plt.ylabel(u'Densidade de potência (W/m²)',fontsize=14)
    plt.title(u'Densidade de potência mensal para {0}'.format(alt),fontsize=18)
    plt.savefig('densidade_potencia_mensal_{0}.png'.format(alt))
    plt.close()

    # Histograma com a frequência relativa por faixa de velocidade do vento
    # (faixas de 1m/s);
    plt.close()
    n_cols = int(np.ceil(df.velocidade.max()))
    plt.hist(df.velocidade, n_cols, range=[0, n_cols], normed=1)
    plt.xticks(range(n_cols+1))
    plt.yticks(np.arange(.1, 1.05, .1), np.arange(.1, 1.05, .1)*100)
    plt.xlabel('Velocidade (m/s)', fontsize=14)
    plt.ylabel(u'Frequência (%)', fontsize=14)
    plt.title(u'Histograma de frequência para {0}'.format(alt), fontsize=18)
    plt.grid()
    plt.savefig('histograma_frequencia_{0}.png'.format(alt))
    plt.close()

    # Gráfico da Frequência acumulada;
    plt.hist(df.velocidade, n_cols, range=[
             0, n_cols], normed=1, cumulative=True)
    plt.xticks(range(n_cols+1))
    plt.yticks(np.arange(.1, 1.05, .1), np.arange(.1, 1.05, .1)*100)
    plt.xlabel('Velocidade (m/s)', fontsize=14)
    plt.ylabel(u'Frequência acumulada (%)', fontsize=14)
    plt.title(
        u'Histograma de frequência acumulada para {0}'.format(alt), fontsize=18)
    plt.grid()
    plt.savefig('histograma_frquencia_acumulada_{0}.png'.format(alt))
    plt.close()

    # Gráfico da Distribuição Weibull para uma altura igual a 10m;
    data = np.sort(df.velocidade)
    expweib = stats.exponweib.fit(data)
    plt.plot(data, stats.exponweib.pdf(data, *expweib))
    plt.grid()
    plt.yticks(np.arange(0, 1, .1))
    plt.xticks(range(0, int(np.ceil(np.max(data)+1))))
    plt.yticks(np.arange(0, 1.05, .1), np.arange(0, 1.05, .1)*100)
    plt.ylabel(u'Frequência (%)', fontsize=14)
    plt.xlabel('Velocidade (m/s)', fontsize=14)
    plt.title(u'Distribuição de Weibull para {0}'.format(alt), fontsize=18)
    plt.savefig('distribuicao_weibull_{0}.png'.format(alt))
    plt.close()

    # Probabilidade de ocorrerem velocidades acima de X m/s para uma altura alt
    print 'Probabilidade de ocorrerem velocidade acima de {0} m/s para uma altura de {1} = {2:.2f}%'.format(X, alt, 100*(1-stats.exponweib.cdf(X, *expweib)))

    return expweib, data, n_cols

anos = range(2002, 2017)

df = pd.read_table('./estacao_82397/hourly_1986_2016.txt', usecols=[0, 1, 2, 3], skiprows=17, delimiter=';', names=[
    'estacao', 'data', 'hora', 'velocidade'], index_col='data')
df2 = pd.read_table('./estacao_82397/hourly_1986_2016.txt', usecols=[0, 1, 2, 3], skiprows=17, delimiter=';', names=[
    'estacao', 'data', 'hora', 'velocidade'], index_col='data')

# alfa = 0.25 considerando considerando espaço aberto com árvores altas
df2.velocidade = df2.velocidade*(50/10.)**0.4

weib1, data1, n_cols1 = pot_eolico(df, anos, '10m', 6)
weib2, data2, n_cols2 = pot_eolico(df2, anos, '50m', 6)

# Gráfico do histograma para as duas situações de altura (10m e 50m)
n_cols = np.max([n_cols1, n_cols2])
plt.hist(df.velocidade, n_cols, range=[0, n_cols], alpha=0.6, normed=True)
plt.hist(df2.velocidade, n_cols, range=[0, n_cols], alpha=0.6, normed=True)
plt.grid()
plt.xticks(range(n_cols+1))
plt.yticks(np.arange(0,1.1,.1),np.arange(0,1.1,.1)*100)
plt.ylabel(u'Frequência (%)',fontsize=14)
plt.xlabel('Velocidade (m/s)', fontsize=14)
plt.title(u'Histograma de frequência para 10m e 50m', fontsize=18)
plt.savefig('histograma_frequencia_10m_50m.png')
plt.close()

# Gráfico da frequência acumulada para as duas situações de altura(10m e 50m);
plt.hist(df.velocidade, n_cols, range=[
         0, n_cols], alpha=0.6, normed=True, cumulative=True)
plt.hist(df2.velocidade, n_cols, range=[
         0, n_cols], alpha=0.6, normed=True, cumulative=True)
plt.grid()
plt.xticks(range(n_cols+1))
plt.yticks(np.arange(0,1.1,.1),np.arange(0,1.1,.1)*100)
plt.xlabel('Velocidade (m/s)', fontsize=14)
plt.ylabel(u'Frequência (%)',fontsize=14)
plt.title(u'Histograma de acumulada para 10m e 50m', fontsize=18)
plt.savefig('histograma_frequencia_10m_50m.png')
plt.close()

# Gráfico da Distribuição Weibull para as duas situações de altura(10m e 50m);
plt.close()
plt.plot(data1, stats.exponweib.pdf(data1, *weib1))
plt.plot(data2, stats.exponweib.pdf(data2, *weib2))
plt.grid()
plt.yticks(np.arange(0,1.1,.1),np.arange(0,1.1,.1)*100)
plt.xticks(range(0,int(np.ceil(np.max([data1,data2])))+1))
plt.ylabel(u'Frequência (%)', fontsize=14)
plt.xlabel('Velocidade (m/s)', fontsize=14)
plt.title(u'Distribuição de Weibull para 10m e 50m', fontsize=18)
plt.savefig('distribuicao_weibull_10m_50m.png')
plt.close()