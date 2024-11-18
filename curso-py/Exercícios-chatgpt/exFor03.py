"""
Exercício 3:
Crie um programa que use um laço for para calcular a soma de todos os números ímpares de 1 a 100 (inclusive).
"""
s = 0
for num in range(1,100):
    if num % 2 != 0:
        s += num
print(s)