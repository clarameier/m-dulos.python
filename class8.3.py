import math

real = float(input('Digite qualquer número real: '))
print('O número digitado por você é lido como {} em sua porção inteira (python math trunc).'.format(math.trunc(real)))
print('O número digitado por você é lido como {} em sua porção inteira (python math floor).'.format(math.floor(real)))
print('O número digitado por você é lido como {} em sua porção inteira (python int).'.format(int(real)))