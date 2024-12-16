valores = []

while True:
    valor = (int(input('Digite um valor: ')))
    if valor not in valores:
        valores.append(valor)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado! Não vou adicionar...')
    escolha = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]

    while escolha not in ['S', 'N']:
        escolha = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]

    if escolha == 'N':
        break
print(sorted(valores))