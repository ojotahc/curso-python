"""
Exercício 4: Soma de Números Ímpares em um Intervalo
Descrição: Crie um programa que leia um número N
e calcule a soma de todos os números ímpares de 1 até N
O programa deve imprimir a soma ao fina
"""

# Solicita ao usuário que insira um número
num = int(input('Digite um número: '))

# Inicializa a variável que armazenará a soma dos números ímpares
s = 0

# Usamos uma variável diferente (i) no for para evitar conflitos com a variável num
for i in range(1, num + 1):  # Percorre todos os números de 1 até num (inclusivo)
    if i % 2 != 0:  # Verifica se i é ímpar
        s += i  # Soma o valor de i a s se i for ímpar

# Imprime o resultado final da soma
print(s)
