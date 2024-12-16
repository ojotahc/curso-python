valores = []


for cont in range(0, 5):
    valores.append(int(input(f'Digite um valor na posição {cont}: ')))

    maior = menor = valores[cont]

    for valor in valores:
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor

print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for i, valor in enumerate(valores):
    if valor == maior:
        print(f'{i}')
print(f'O menor valor digitado foi {menor} nas posições ',end='')
for i, valor in enumerate(valores):
    if valor == menor:
        print(f'{i}')




