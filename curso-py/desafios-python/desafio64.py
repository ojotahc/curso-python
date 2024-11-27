flag = False
cont = 0
soma = 0

while flag != True:
    n =int(input('Digite um número [999 para parar]: '))
    if n == 999:
        n = 0
        flag = True
    cont += 1
    soma += n
    #print(n)

print('Você digitou {} números e a soma entre eles foi {}.'.format(cont - 1, soma))
