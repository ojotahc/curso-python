# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
from random import choice
nome = str(input(('Primeiro aluno: ')))
nome2 = str(input(('Segundo aluno: ')))
nome3 = str(input(('Terceiro aluno: ')))
nome4 = str(input(('Quarto aluno: ')))
lista = [nome, nome2, nome3, nome4]
sorteio = choice(lista)
print('O aluno escolhido foi', sorteio)
