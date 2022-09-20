from math import hypot

#modo manual
oposto = float(input('Digite o valor do comprimento, em metros quadrados, do cateto oposto: '))
adja = float(input('Digite o valor do comprimento, em metros quadrados, do cateto adjacente: '))
hipo = (oposto ** 2 + adja ** 2) ** (1/2)
print('O valor da hipotenusa do seu triângulo retângulo equivale a {:.2f}m²!'.format(hipo))

#modo import math
oposto = float(input('Digite o valor do comprimento, em metros quadrados, do cateto oposto: '))
adja = float(input('Digite o valor do comprimento, em metros quadrados, do cateto adjacente: '))
hipo = hypot(oposto, adja)
print('O valor da hipotenusa do seu triângulo retângulo equivale a {:.2f}m²!'.format(hipo))
