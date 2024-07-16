"""
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
- IMC abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida
"""

peso = float(input('Qual é o seu peso? (KG) '))
altura = float(input('Qual é a sua altura? (m) '))
# Calculando o IMC
imc = peso / (altura ** 2)
# Arredondando o IMC para duas casas decimais
imc = round(imc, 2)
print('O IMC dessa pessoa é de {:.2f}.'.format(imc))
if imc < 18.5:
    print('O peso dessa pessoa está ABAIXO do peso NORMAL. CUIDADO!')
elif imc < 25:
    print('O peso dessa pessoa está NORMAL. PARABÉNS!')
elif imc < 30:
    print('Essa pessoa está com sobrepeso. Tenha cuidado!')
elif imc < 35:
    print('Essa pessoa está com obesidade grau 1. CUIDADO!')
elif imc < 40:
    print('Essa pessoa está com obesidade grau 2. CUIDADO!')
else:
    print('Essa pessoa está com obesidade grau 3. CUIDADO!')

