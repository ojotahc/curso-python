"""
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
"""
"""
Versão Guanabara

salario = float(input('Qual é o salário do funcionário? R$'))
if salario <=1250:
    novo  = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salario, novo))

OBS: Posso declarar as variáveis depois!!!
"""

salario = float(input('Qual é o salário do funcionário? R$'))
# vamos usar essa variável se o salário for menor ou igual a R$1250,00
aumento_Maior = float(salario * 0.15)
# vamos usar essa variável se o salário for maior do que R$1250,00
aumento_Menor = float(salario * 0.10)
# vai armazenar o valor do salário antigo mais o aumento
salario_Aumento_Maior = float(salario + aumento_Maior)
salario_Aumento_Menor = float(salario + aumento_Menor)


if salario <= 1250:
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salario, salario_Aumento_Maior))
else:
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salario, salario_Aumento_Menor))

