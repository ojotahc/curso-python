# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as
v = input('Digite algo: ')
print('O tipo primitivo desse valor é:', type(v))
print('É um número? ', v.isnumeric())
print('É alfanumérico? ', v.isalnum())
print('É alfabético? ', v.isalpha())
print('É um número decimal', v.isdecimal())
print('Está em maiúscula?', v. isupper())
