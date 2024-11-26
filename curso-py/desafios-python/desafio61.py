# Desafio 61

"""
a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
for c in range(1,11):
    print(a1 + (c - 1)* r, end=' -> ')
"""
# an ​= a1 ​+ (n−1)⋅r


a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
contador = 1


while contador <= 10:
  contador += 1
  a1 += r
  print(a1, end=' -> ')
