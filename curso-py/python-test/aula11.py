# Se a estrutura condicional conter somente o if, ela é uma estrutura simples.
# Se conter um if e um else, ela é composta.
# Se conter um if, elif e um else, ela é aninhada.

nome = str(input('Qual é o seu nome? '))
if nome == 'João':
    print('Que bonito nome!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Cláudia Jéssica Júlia':
    print('Belo nome feminino!')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))