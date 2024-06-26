# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
nome = str(input('Digite seu nome completo: ')).strip()
# Tratar a string dessa forma para evitar erros
print('SILVA' in nome.upper())
