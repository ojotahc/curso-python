#  Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.
s = 0
for c in range(1*3,500,2*3):
    print(c)
    s = s + c # também pode ser s += c
print('A soma entre todos os valores foi {}'.format(s))
