"""
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""
"""
Essa foi a primeira versão sem o módulo randint
from random import choice
print('VOU PENSAR EM UM NÚMERO ENTRE 0 E 5. TENTE ADVINHAR...')
num = [0, 1, 2, 3, 4, 5]
sorteio = choice(num)
chute = int(input('Qual é o seu chute?: '))
print('PROCESSANDO...')

if chute == sorteio:
    print('Você acertou!')
else:
    print('Você errou! Eu pensei no número {}'.format(sorteio))
"""

from random import randint, choice
from time import sleep
print('VOU PENSAR EM UM NÚMERO ENTRE 0 E 5. TENTE ADVINHAR...')
num = randint(0, 5)  # Faz o computador "PENSAR"

chute = int(input('Qual é o seu chute?: '))
print('PROCESSANDO...')
sleep(2)  # Importando a biblioteca sleep posso fazer o computador esperar
if chute == num:
    print('Você acertou!')
else:
    print('Você errou! Eu pensei no número {}!'.format(num))
