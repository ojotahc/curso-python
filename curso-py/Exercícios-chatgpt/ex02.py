# Solicita ao usuário que insira um número
numero = int(input("Digite um número: "))

# Verifica se o número é par ou ímpar
if numero % 2 == 0:
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")
# Quando você usa o operador % (módulo) em numero % 2, você está realizando a divisão do número por 2, mas ao invés de obter o quociente (o resultado da divisão), você está interessado apenas no resto dessa divisão.