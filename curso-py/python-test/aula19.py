dados = {'nome':'Pedro', 'idade':25}
print(dados['nome'])
print(dados['idade'])

# o append não funciona no dicionário. Posso criar o seguinte comando:
dados['sexo'] = 'M'
print(dados)

# Para remover algum item, utilizo o del
del dados['idade']

filmes = {'titulo':'StarWars',
          'ano':1997,
          'diretor':'George Lucas',
          }

print(filmes.values())
print(filmes.keys())
print(filmes.items())

for k, v in filmes.items():
    print(f'O {k} é {v}')