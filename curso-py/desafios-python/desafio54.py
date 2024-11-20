"""
from datetime import date
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano == date.today().year
"""


from datetime import date
maior = 0
menor = 0

for c in range(1, 8):
    nascimento = int(input('Em que ano a {}ª pessoa nasceu? '.format(c)))
    if date.today().year - nascimento < 21:
        menor += 1
    else:
        maior += 1  # Não precisa da comparação ">= 21", basta ver se a pessoa é maior ou igual a 18
print('Ao todo tivemos {} pessoas maiores de idade.'.format(maior))
print('E também tivemos {} pessoas menores de idade'.format(menor))
