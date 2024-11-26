n = int(input('Digite um número [999 para parar]: '))
flag = False
cont = 0

while flag != True:
    n = int(input('Digite um número [999 para parar]: '))
    if n == 999:
        flag = True


print('Você digitou {} números e a soma entre eles foi {}.'.format())