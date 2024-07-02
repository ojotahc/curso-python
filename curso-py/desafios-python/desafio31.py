"""
Desenvolva um programa que pergunte a distância de uma viagem em Km. 
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
"""
# Minha versão desse programa
km_Viagem = float(input('Qual é a distância da sua viagem? '))
viagem_Padrao = float(km_Viagem) * 0.50
viagem_Longa = float(km_Viagem) * 0.45
if km_Viagem <= 200:
  print('Você está prestes a começar uma viagem de {:.2f}Km.E o preço da sua passagem será de R${:.2f}'.format(km_Viagem, viagem_Padrao))
else:
  print('Você está prestes a começar uma viagem de {:.2f}Km.E o preço da sua passagem será de R${:.2f}'.format(km_Viagem, viagem_Longa))
# Versão Gunabara
"""
distancia = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}Km.'.format(distancia))
if distancia <= 200:
  preco = distancia * 0.50
else:
  preco = distancia * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preco))

"""