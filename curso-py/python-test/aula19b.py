pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
pessoas['nome'] = 'Leandro'
pessoas['peso'] = 98.5
# na hora de referenciar os elementos, uso colchetes e na hora de declarar chaves
print(f'O pessoas{["nome"]} tem {["idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

for k, v in pessoas.items():
    print(f'{k} = {v}')