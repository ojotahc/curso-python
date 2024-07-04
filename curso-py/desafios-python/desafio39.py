"""
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""
from datetime import date

# Entrada do ano de nascimento
ano_Nascimento = int(input('Ano de Nascimento: '))
# Ano atual
ano_Atual = date.today().year
# Calculo da idade
idade = ano_Atual - ano_Nascimento

# Determinação do status do alistamento e calculo da diferença de anos
if idade == 18:
    print('Quem nasceu em {} tem {} anos em {}.'.format(ano_Nascimento, idade, ano_Atual))
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    diferenca_idade = 18 - idade  # Calculo correto para quem ainda não tem 18 anos
    print('Quem nasceu em {} tem {} anos em {}.'.format(ano_Nascimento, idade, ano_Atual))
    print('Ainda falta(m) {} ano(s) para o alistamento.'.format(diferenca_idade))
    print('Seu alistamento será em {}.'.format(ano_Atual + diferenca_idade))
elif idade > 18:
    diferenca_idade = idade - 18  # Calculo correto para quem já passou dos 18 anos
    print('Quem nasceu em {} tem {} anos em {}.'.format(ano_Nascimento, idade, ano_Atual))
    print('Você já deveria ter se alistado há {} ano(s).'.format(diferenca_idade))
    print('Seu ano de alistamento foi em {}.'.format(ano_Atual - diferenca_idade))


