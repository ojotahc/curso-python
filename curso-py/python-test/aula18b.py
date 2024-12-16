teste = list()
teste.append('Gustavo')
teste.append(40)

galera = list()
# é importante usar o [:] para criar uma cópia
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)
