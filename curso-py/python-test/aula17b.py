valores = []

#valores.append(5)
#valores.append(9)
#valores.append(4)



for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, valor in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {valor}!')