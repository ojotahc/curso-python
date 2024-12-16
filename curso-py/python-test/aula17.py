num = [2, 5, 9, 1]
num[2] = 3

# adicionando o valor 7 à lista
num.append(7)

# colocando em ordem crescente
# num.sort()

# colocando em ordem decrescente
num.sort(reverse=True)

# Inserindo valores em posições específicas
num.insert(2, 2)

# Removendo elementos
num.pop()

if 4 in num:
    num.remove(5)
else:
    print('Não achei o número 5')

print(num)
print(f'Essa lista tem {len(num)} elementos.')