# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
c = float(input('Digite a temperatura: '))
f = (c * (9/5)) + 32
print('{}C é igual a {}F'.format(c, f))
