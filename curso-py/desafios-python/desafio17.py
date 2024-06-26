from math import sqrt
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
h = sqrt(pow(co, 2) + pow(ca, 2))
print('O valor da Hipotenusa é {:.2f}'.format(h))
