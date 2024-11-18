"""
Exercício 1:
Crie um programa que use um laço for para iterar sobre a lista de números e imprima apenas os números pares.
"""
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for numero in numeros:  # Iterando sobre a lista
    if numero % 2 == 0:  # Verificando se o número é par
        print(numero)