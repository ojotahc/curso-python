# Consigo criar alinhamentos, basta escolher a quantidade de caracteres
nome = input('Qual é o seu nome? ')
print('Prazer em conhecer você {:20}!'.format(nome))

nome = input('Qual é o seu nome? ')
print('Prazer em conhecer você {:>20}!'.format(nome))

nome = input('Qual é o seu nome? ')
print('Prazer em conhecer você {:<20}!'.format(nome))

nome = input('Qual é o seu nome? ')
print('Prazer em conhecer você {:=^20}!'.format(nome))
