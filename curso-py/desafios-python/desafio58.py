# Desafio 58
from random import randint
from time import sleep

cont_palpite = 1
jogador = 0

computador = randint(0, 10)
print('VOU PENSAR EM UM NÚMERO DE 0 A 10.')
print('TENTE ADVINHAR!!!')
sleep(1)
print('PENSANDO...')
sleep(2)
jogador = int(input('Qual o seu palpite? '))


while jogador != computador:
  cont_palpite += 1
  if jogador < computador:
    print('Mais...')
  else:
    print('Menos...')  
  jogador = int(input('Você errou, tente novamente! '))
print('PARABÉNS!!!')
print('VOCÊ ACERTOU! O NÚMERO QUE EU PENSEI FOI {}'.format(computador))
print('Você precisou de {} tentativa(s) para acertar.'.format(cont_palpite))