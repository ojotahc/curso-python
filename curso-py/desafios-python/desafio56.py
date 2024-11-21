# meu código com alguns erros
"""
media = 0
maior_idade = 0
mais_velho = 0
cont_feminino = 0

for p in range(1, 5):
  print('----- {}ª PESSOA -----'.format(p))
  nome = str(input('Digite o nome: ')).strip()
  idade = int(input('Digite a idade: '))
  sexo = str(input('Digite o sexo [M/F]: ')).strip()
  media += idade / 4
  if sexo == 'M':
    if p == 1:
      maior_idade = idade
    else:
      if idade > maior_idade:
        maior_idade = idade
        if nome == nome:
          mais_velho = nome

  if sexo == 'F':
    if idade < 20:
      cont_feminino += 1


print('A média do grupo é {} anos'.format(media))
print('O homem mais velho tem {} anos e se chama {}'.format(maior_idade, mais_velho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(cont_feminino))

"""
# versão corrigida
soma_idade = 0
maior_idade = 0
mais_velho = ""
cont_feminino = 0

for p in range(1, 5):
  print('----- {}ª PESSOA -----'.format(p))
  nome = input('Digite o nome: ').strip()
  idade = int(input('Digite a idade: '))
  sexo = input('Digite o sexo [M/F]: ').strip().upper()

  # Somando a idade de todos para calcular a média depois
  soma_idade += idade

  # Verificando o homem mais velho
  if sexo == 'M' and idade > maior_idade:
    maior_idade = idade
    mais_velho = nome

  # Contando mulheres com menos de 20 anos
  if sexo == 'F' and idade < 20:
    cont_feminino += 1

# Calculando a média depois de somar todas as idades
media = soma_idade / 4

print('A média do grupo é {} anos'.format(media))
print('O homem mais velho tem {} anos e se chama {}'.format(maior_idade, mais_velho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(cont_feminino))

