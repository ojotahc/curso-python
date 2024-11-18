"""
from datetime import date
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano == date.today().year
"""
from datetime import date
ano_atual = date.today().year
menor = 0
maior = 0

for c in range(1,8):
    ano = int(input('Em que ano a {}ª pessoa nasceu? '.format(c)))
    idade = ano_atual - ano
    if idade >= 21:
        maior +=1
    else:
        menor +=1
print(maior)
print(menor)