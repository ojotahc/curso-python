num = int(input('Digite um valor: '))
num2 = int(input('Digite outro valor: '))
num3  = int(input('Digite mais um valor: '))
num4 = int(input('Digite o último valor: '))

numeros = (num, num2, num3, num4)
print(f'O valor 9 apareceu {numeros.count(9)} vezes.')
if 3 in numeros:
    print(f'O valor 3 apareceu {numeros.index(3)+1}ª posição.')
else:
   print('o Valor 3 não foi digitado em nenhuma posição') 
print('Os valores pares digitados foram ', end='')
for n in numeros:
    if n % 2 == 0:
        print(n, end= ' ')