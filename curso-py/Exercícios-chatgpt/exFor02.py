"""
Exercício 2:
Crie um programa que use um laço for para imprimir os números de 1 a 10, mas, para os números múltiplos de 3, imprima a palavra "Fizz", e para os números múltiplos de 5, imprima a palavra "Buzz". Se o número for múltiplo de 3 e 5, imprima "FizzBuzz".
"""
for num in range(1, 11):
    if num % 3 == 0 and num % 5 == 0:  # Verificando múltiplos de 3 e 5 primeiro
        print('FizzBuzz')
    elif num % 3 == 0:
        print('Fizz')
    elif num % 5 == 0:
        print('Buzz')
    else:
        print(num)  # Para os números que não são múltiplos de 3 nem 5
