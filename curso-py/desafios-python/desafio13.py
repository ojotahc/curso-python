salario = float(input('Digite o seu salário: '))
aumento = float(salario * 0.15)
salarioAumento = float(salario + aumento)
# aumento = salario * 15 / 100

print('Seu novo salário com 15% de aumento é {:.2f}'.format(salarioAumento))
