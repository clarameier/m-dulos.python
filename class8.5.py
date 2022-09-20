import math

angulo = float(input('Digite um valor de um ângulo: '))

sen = math.sin(math.radians(angulo))
print('O ângulo de {} tem o seno de {:.2f}.'.format(angulo, sen))

cosen = math.cos(math.radians(angulo))
print('O ângulo de {} tem o cosseno de {:.2f}.'.format(angulo, cosen))

tang = math.tan(math.radians(angulo))
print('O ângulo de {} tem o tangente de {:.2f}.'.format(angulo, tang))

