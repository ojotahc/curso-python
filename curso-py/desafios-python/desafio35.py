#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
"""
a+b>c
a+c>ba+c>b
b+c>ab+c>a

"""

print('-='*20)
print('ANALISADOR DE TRIÂNGULO')
print('-='*20)

primeiro = float(input('Primeiro segmento: '))
segundo = float(input('Segundo segmento: '))
terceiro = float(input('Terceiro segmento: '))

if primeiro + segundo > terceiro and primeiro + terceiro > segundo and segundo + terceiro > primeiro:
    print('Os segmentos acima PODEM FORMA um triângulo!')
else:
     print('Os segmentos acima NÃO PODEM FORMAR um triângulo!')



