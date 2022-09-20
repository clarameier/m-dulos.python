from random import choice

nome1 = str(input('Primeiro aluno: '))
nome2 = str(input('Segundo aluno: '))
nome3 = str(input('Terceiro aluno: '))
nome4 = str(input('Quarto aluno: '))

alunos = [nome1, nome2, nome3, nome4]
sorteio = choice(alunos)

print('O (a) aluno (a) sorteado (a) para apagar o quadro foi {}!'.format(sorteio))