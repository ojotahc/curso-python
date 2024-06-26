'''
Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao todo (sem considerar espaços).
- Quantas letras tem o primeiro nome.

REVISAR AULA 09

'''
# Utilizando o método strip para elimnar possíveis espaços
nome = str(input('Digite o seu nome completo: ')).strip()
# Variável criada para separar e criar uma lista de strings
divido = nome.split()

# Variável para juntar as strings da lista da variavel divido, porém removendo os espaços entre as strings
resultado = ''.join(divido)

print(nome.upper())
print(nome.lower())
print('{} possui {} letras'.format(nome, len(resultado)))
print('O primeiro nome possui {} letras'.format(len(divido[0])))
