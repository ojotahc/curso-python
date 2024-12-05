from random import sample

# Lista de números de 1 a 10
numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# Sorteando 5 números aleatórios da lista
resultado = sample(numeros, 5)

# Imprimindo os números sorteados
print(f'Números sorteados: ', end='')
for n in resultado:
    print(f'{n}', end=' ')

# Encontrando o maior e o menor valor
maior = menor = resultado[0]

for n in resultado:
    if n > maior:
        maior = n
    if n < menor:
        menor = n

# Exibindo o maior e o menor valor
print(f'\nMaior valor: {maior}')
print(f'Menor valor: {menor}')