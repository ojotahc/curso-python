# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
grana = float(input('Digite quanto você tem na carteira: R$'))
doletas = float(grana / 5.37)


print('Você pode comprar {:.2f} doletas'.format(doletas))
