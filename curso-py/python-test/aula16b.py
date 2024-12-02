# Tuplas - variável que guarda mais de um valor
# Tuplas são imutáveis

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')

# coloca em ordem
print(sorted(lanche))

a = (2, 5, 4)
b = (5, 8, 1, 2)

c = b + a

print(c)
print(c.count(4))
print(c.index(8))

pessoa = ('Gustavo', 39, 'M', 99.88)
print(pessoa)

# del(pessoa) - apago da memória