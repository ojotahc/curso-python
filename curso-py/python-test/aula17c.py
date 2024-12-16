# Se eu fazer com que uma lista receba outra, e eu mudo algo dentro da segunda, a primeira lista tbm muda - Pyhton cria uma ligação

# Criando cópia de forma certa
a = [2, 3, 4, 7]

# Pegando todos os valores de a e jogando em b
b = a[:]
b[2] = 8

print(f'Lista A: {a}')
print(f'Lista B: {b}')