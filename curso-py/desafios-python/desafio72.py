seq = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove',
       'dez', 'onze', 'doze', 'treze', 'Catorze', 'quinze', 'dezesseis', 'dezessete',
       'dezoito', 'dezenove','vinte')

num = int(input('Digite um número entre 0 e 20: '))
while num < 0 or num > 20:
    num = int(input('Valor inválido! Por favor, digite um número entre 0 e 20: '))
print(f'Você digitou o número {seq[num]}.')
