from random import shuffle
# O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
# usei a função shuffle para embaralhar
nome = str(input(('Primeiro aluno: ')))
nome2 = str(input(('Segundo aluno: ')))
nome3 = str(input(('Terceiro aluno: ')))
nome4 = str(input(('Quarto aluno: ')))
lista = [nome, nome2, nome3, nome4]
shuffle(lista)
print('A ordem da apresentação será:')
print(lista)
