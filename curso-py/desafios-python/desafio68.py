from random import randint

computador = randint(0, 10)
jogador = int(input('Diga um valor: '))
escolha = str(input('Par ou Ímpar? [P/I]: ')).strip().upper()[0]
print()
cont_vitoria = 0

while True:
    total = jogador + computador
    if escolha == 'P' and (jogador + computador) % 2 == 0:
        print(f'Você jogou {jogador} e o computador {computador}. Total de {total} deu PAR.')
        print('Você venceu!\n Vamos jogar novamente...')
        cont_vitoria += 1
        print()
        jogador = int(input('Diga um valor: '))
        escolha = str(input('Par ou Ímpar? [P/I]: ')).strip().upper()[0]
    elif escolha == 'I' and (jogador + computador) % 2 != 0:
        print(f'Você jogou {jogador} e o computador {computador}. Total de {total} deu ÍMPAR.')
        print('Você venceu!\n Vamos jogar novamente...')
        cont_vitoria += 1
        print()
        jogador = int(input('Diga um valor: '))
        escolha = str(input('Par ou Ímpar? [P/I]: ')).strip().upper()[0]
        print()
    elif escolha == 'P' and (jogador + computador) % 2 != 0:
        print(f'Você jogou {jogador} e o computador {computador}. Total de {total} deu ÍMPAR.')
        print('Você Perdeu!')
        break
    elif escolha == 'I' and (jogador + computador) % 2 == 0:
        print(f'Você jogou {jogador} e o computador {computador}. Total de {total} deu PAR.')
        print('Você Perdeu!')
        break
print(f'GAME OVER! Você venceu {cont_vitoria} vez(es).')