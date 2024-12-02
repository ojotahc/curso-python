total_compra = 0
total_produto_mais_de_mil = 0
menor_preco = 0
cont = 0
nome_produto_barato = ''
# obs: para conseguir pegar o valor menor e seu nome preciso do contador pra saber qual é o o primeiro produto
while True:
    nome_produto = str(input('Nome do Produto: '))
    preco_poduto = float(input('Preço: '))
    cont += 1

    if preco_poduto > 1000:
        total_produto_mais_de_mil += 1

    if cont == 1:
        menor_preco = preco_poduto
        nome_produto_barato = nome_produto
    else:
        if preco_poduto < menor_preco:
            menor_preco = preco_poduto
            nome_produto_barato = nome_produto

    escolha = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    print('-'*25)

    total_compra += preco_poduto

    # Validação da resposta para continuar ou encerrar o cadastro
    while escolha not in ['S', 'N']:
        escolha = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    
    # Se a resposta for 'N', encerra o loop
    if escolha == 'N':
        break

print(f'O total da compra foi R${total_compra}.')
print(f'Temos {total_produto_mais_de_mil} produto(s) custando mais que R$1.000.00.')
print(f'O produto mais barato foi {nome_produto_barato} que custa {menor_preco}.')