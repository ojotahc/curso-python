"""
Exercício 5: Soma dos Números Pares em um Intervalo
Descrição: Crie um programa que leia um número N e calcule a soma de todos os números pares de 1 até N.
O programa deve imprimir a soma ao final.

"""
num = int(input('Digite um número: '))
s = 0
for c in range(1,num+1):
    if c % 2 == 0:
        s += c
print('A soma de todos os números pares é {}.'.format(s))

 