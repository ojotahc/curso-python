cont = 0
soma = 0
dec = str()
maior = 0
menor = 0

while dec != 'N':
    num = int(input('Digite um número: '))
    dec = str(input('Quer continuar? [S/N] ')).upper().strip()[0]

    cont += 1
    soma += num
    
    # Atualiza maior e menor na primeira entrada
    if cont == 1:  # No primeiro número, inicializa ambos
        maior = menor = num
    else:
        # Compara para encontrar o maior e o menor
        if num > maior:
            maior = num
        if num < menor:
            menor = num

media = soma / cont

print('Você digitou {} números e a média foi {}'.format(cont, media))
print('O mairo valor foi {} e o menor foi {}.'.format(maior, menor))


