n1 = int(input('Digite um número: '))

dobro = n1 * 2
triplo = n1 * 3
raiz = n1 ** (1/2)

# posso fazer a raiz com a função pow(n1, (1/2))

print('O dobro de {} é {}, seu triplo é {} e sua raiz é {:.3f}'.format(
    n1, dobro, triplo, raiz))
