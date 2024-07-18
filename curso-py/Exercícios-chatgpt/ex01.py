# Escreva um programa que peça ao usuário para inserir três números e depois calcule e imprima a média deles.
n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))
n3 = float(input('Digite o terceiro valor: '))
media = (n1 + n2 + n3) / 3
print(f'A média entre os três valores foi {round(media, 2)}.')

# Você poderia arredondar o resultado da média para tornar a saída mais agradável, se necessário. Por exemplo, usando a função round().
# O argumento 2 no round() especifica que a média será arredondada para duas casas decimais.