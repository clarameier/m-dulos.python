numero = int(input('Digite um número de 0 a 9999, por favor: '))
n = str(numero)

#unidade
print('Sua unidade é de: {}.'.format(n[3]))

#dezena
print('Sua dezena é de: {}.'.format(n[2]))

#centena
print('Sua centena é de: {}.'.format(n[1]))

#milhar
print('Seu milhar é de: {}.'.format(n[0]))
