frase = str(input('Digite um frase: '))
invertido = ''
for caractere in frase:
    invertido = caractere + invertido
if frase == invertido:
    print('O inverso de {} é {}'.format(frase, invertido))
    print('Temos um palíndromo')
else:
    print('Não temos um palíndromo')