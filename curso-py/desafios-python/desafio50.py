'''
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
'''
soma = 0 # Acumulador é incrementado
cont = 0 # conta quantas vezes foi incrementado
for c in range(1, 7):
  num = int(input('Digite um valor: '))
  if num % 2 == 0:
    soma += num
    cont += 1
print('Você informou {} números e a soma é {}.'.format(cont, soma))