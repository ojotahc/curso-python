valores = []

while True:
    valor = int(input('Digite um valor: '))
    valores.append(valor)
    valores.sort(reverse=True)

    escolha = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]

    while escolha not in ['N', 'S']:
        escolha = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]

    if escolha == 'N':
        break
print(f'Você digitou {len(valores)} elementos.')
print(f'Os valores em ordem decrescente são {valores}')
if 5 in valores:
    print('O valor 5 foi encontrado na lista!')
else:
    print('O valor 5 não foi encontrado na lista!')
