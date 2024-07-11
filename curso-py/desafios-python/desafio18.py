# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
# Dica: O grau no caso tem que ser radiano, se declararmos sem a função radiano, o python interpreta como centigrados
from math import sin, cos, tan, radians
a = float(input('Digite o valor do ângulo: '))
s = sin(radians(a))
c = cos(radians(a))
t = tan(radians(a))
print('O seno, cosseno e tangente de {} é {:.2f}, {:.2f} e {:.2f}'.format(a, s, c, t))
