# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#- Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JÚNIOR
# - Até 25 anos: SÊNIOR
# - Acima de 25 anos: MASTER

idade = int(input('Digite a idade do atleta: '))

if idade <= 9:
    print('o atleta tem {} anos.'.format(idade))
    print('Classificação: MIRIM')
elif idade >= 10 and idade <= 14:
    print('O atleta tem {} anos.'.format(idade))
    print('Classificação: INFANTIL')
elif idade >= 15 and idade <= 19:
    print('O atleta tem {} anos.'.format(idade))
    print('Classificação: JÚNIOR')
elif idade >= 20 and idade <= 25:
    print('O atleta tem {} anos.'.format(idade))
    print('Classificação: SÊNIOR')
else:
    print('O atleta tem {} anos.'.format(idade))
    print('Classificação: MASTER')

"""
VERSÂO GUANABARA

from datetime importe date
atual = date.today().year
nascimento = int(input('Ano nascimento: '))
idade = atual - nascimento
print('O atleta tem {} anos.'.format(idade))

if idade <=9:
    print('Classificação: MIRIM')
elif idade <=14:

"""