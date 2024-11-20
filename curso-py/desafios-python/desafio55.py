# Inicializamos as variáveis 'maior' e 'menor' para armazenar os valores do maior e menor peso.
maior = 0
menor = 0

# Usamos um laço 'for' para iterar de 1 a 5 (representando as 5 pessoas).
for pess in range(1, 6):
    # Solicitamos ao usuário o peso da pessoa atual. A entrada é convertida para tipo float.
    peso = float(input('Peso da {}ª pessoa: '.format(pess)))
    
    # Na primeira pessoa (quando pess == 1), inicializamos 'maior' e 'menor' com o peso dela.
    if pess == 1:
        maior = peso  # O peso da primeira pessoa é considerado o maior inicialmente.
        menor = peso  # O peso da primeira pessoa é considerado o menor inicialmente.
    else:
        # Se o peso atual for maior que o 'maior' registrado, atualizamos a variável.
        if peso > maior:
            maior = peso
        # Se o peso atual for menor que o 'menor' registrado, atualizamos a variável.
        if peso < menor:
            menor = peso

# Após o término do laço, exibimos o maior e o menor peso registrados.
print('O maior peso registrado foi: {:.2f} kg'.format(maior))
print('O menor peso registrado foi: {:.2f} kg'.format(menor))
