nome = str(input('Digite o seu nome completo, por favor: ')).strip()

#nome em maiúsculo:
print(nome.upper())

#nome em minúsculo
print(nome.lower())

#contagem de letras do nome (incluindo os espaços)
print(len(nome))

#contagem de letras do nome (sem incluir os espaços)
print(len(nome) - nome.count(' '))

#contagem de letras do primeiro nome
print(nome.find(' '))