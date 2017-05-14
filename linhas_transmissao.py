# -*- coding: utf-8 -*-
from math import pi
import numpy as np

# Dados de entrada
print 'Valores do recptor'
Vr = float(raw_input('Tensão (kV) = '))*1e3
Sr = float(raw_input('Potência aparente (MVA) = '))*1e6
FP = float(raw_input('Fator de potência (%) = '))/1e2
f = float(raw_input('Frequência (Hz) = '))

print 'Paraêmetros da linha'
r = float(raw_input('r (ohm/km) = '))
L = float(raw_input('L (mH/km) = '))/1e3
C = float(raw_input('C (uF/km) = '))/1e6
g = float(raw_input('g (uS/km) = '))
x = float(raw_input('comprimento da linha (km) = '))

''' valores de exemplo
r = 0.11 ohm/km
C = 1.385*1e-3 H/km
C = 0.00935*1e-6 G/km
f = 60 Hz
g = 0
V = 250*1e-3 Classe da linha
Vr = 220*10e3 Tensão no receptor em Volts
Sr = 180*10e6 Potência aparente no receptor
FP = 0.92 Fator de potência
x = 320 Comprimento da linha em km
'''
print 'RESULTADOS'

#Omega
omega = 2*pi*f
print 'Omega = %.3f rad/s' % (omega)

#impedância série
z = r + omega*L*1j
print 'z = %.3f/_%.3fº ohm/km' % (np.abs(z),np.angle(z)*180/pi)

#admitância shunt
y = g + omega*C*1j
print 'y = %.3f/_%.3fº uS/km' % (np.abs(y)*1e6,np.angle(y)*180/pi)

#Constante de propagação
gama = np.sqrt(z*y)
print 'gama = %.3f/_%.3fº ' % (np.abs(gama), np.angle(gama)*180/pi)

#impedância característica
Zc =  np.sqrt(z/y)
print 'Zc = %.3f/_%.3fº ohm' % (np.abs(Zc), np.angle(Zc)*180/pi)

Ir = Sr/(np.sqrt(3)*Vr)
theta = np.arccos(FP)
Vr = Vr/(np.sqrt(3))

def cart2pol(x,y):
	rho = np.sqrt(x**2 + y**2)
	phi = np.arctan2(y, x)
	return rho, phi

def pol2cart(rho,phi):
	x = rho*np.cos(phi)
	y = rho*np.sin(phi)
	return x,y

ix, iy = pol2cart(-theta, Ir)
I = np.complex(ix, iy)
print 'Ir = %.3f/_%.3fº A' % (np.abs(I), np.angle(I)*180/pi)
print 'Vr = %.3f kV' % (Vr/1e3)

senh = np.sinh(gama*x)
print 'sinh = %.3f/_%.3fº' % (np.abs(senh),np.angle(senh)*180/pi)
cosh = np.cosh(gama*x)
print 'cosh = %.3f/_%.3f' % (np.abs(cosh),np.angle(cosh)*180/pi)

Ix = (1/Zc)*senh*Vr+cosh*I
Vx = cosh*Vr+Zc*senh*I

absVx = np.abs(Vx)/1e3
angleVx = np.angle(Vx)*180/pi
absIx = np.abs(Ix)
angleIx = np.angle(Ix)*180/pi

print 'A tensão no transmissor é %.3f/_%.3fº kV' % (absVx,angleVx)
print 'A corrente no transmissor é %.3f/_%.3fº A' % (absIx, angleIx)

Sx = Vx*np.conj(Ix)
print 'S = %.3f/_%.3fº MVA' % (np.abs(Sx)/1e6, np.angle(Sx)*180/pi)
S3f = 3*Sx
print 'S3f = %.3f/_%.3fº MVA' % (np.abs(S3f)/1e6, np.angle(S3f)*180/pi)
P3f = np.real(S3f)
print 'P3f = %.3f MW' % (P3f/1e6)
Q3f = np.imag(S3f)
print 'Q3f = %.3f MVAr' % (Q3f/1e6)

P = Sr*FP/1e6
print 'Potência ativa no receptor = %.3f MW' % (P)

rendimento = (1-(P3f-Sr*FP)/P3f)*100
print 'Rendimento = %.3f' % (rendimento)