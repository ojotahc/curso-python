dados = list()
pessoas = list()

"""
dados.append('Pedro')
dados.append(25)
"""


# estou criando um cópia de dados dentro de pessoas
pessoas.append(dados[:])

# adicionando vários elementos
pessoas = [['Pedro', 25], ['Maria', 19], ['João', 32]]

print(pessoas[0][0])
print(pessoas[1][1])
print(pessoas[2][0])
print(pessoas[1])