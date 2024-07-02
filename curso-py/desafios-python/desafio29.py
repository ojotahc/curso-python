"""
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.
"""

velocidade_Carro = int(input('Qual é a velocidade atual do carro?: '))
limite = int(80)
multa = int(velocidade_Carro - limite) * 7
if velocidade_Carro <= limite:
  print('Tenha um bom dia! Dirija com segurança!')
else:
  print('MULTADO! Você excedeu o imite permitido que é 80Km/h. Você deve pagar uma multa de R${:.2F}!'.format(multa))