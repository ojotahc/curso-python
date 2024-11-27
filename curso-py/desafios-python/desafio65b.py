cont = 0  # Contador para o número de valores digitados
soma = 0  # Soma de todos os números digitados
dec = 'S'  # Inicialização da decisão para entrar no loop
maior = 0  # Inicializa o maior valor
menor = 0  # Inicializa o menor valor

while dec == 'S':
    num = int(input('Digite um número: '))  # Lê o número do usuário

    # Atualiza o contador e a soma
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

    # Pergunta ao usuário se ele deseja continuar
    dec = str(input('Quer continuar? [S/N] ')).strip().upper()

# Calcula a média
media = soma / cont

# Exibe os resultados
print('Você digitou {} números e a média foi {:.2f}.'.format(cont, media))
print('O maior valor foi {} e o menor foi {}.'.format(maior, menor))
