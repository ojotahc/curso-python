# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
# Solicita as notas ao usuário
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))

# Calcula a média
m = (n1 + n2) / 2

# Exibe o resultado
print('A média é {:.2f}'.format(m))
