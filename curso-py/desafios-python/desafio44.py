valor_compras = float(input('Preço das compras: R$'))
print('FORMAS DE PAGAMENTO')
print('[ 1 ] à vista dinheiro/cheque')
print('[ 2 ] à vista cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x vezes ou mais no cartão')
forma_pagamento = int(input('Qual a forma de pagamento? '))

if forma_pagamento == 1:
    print('O valor total é R${:.2f}, à vista no dinheiro/cheque tem 10% desconto.'.format(valor_compras-(10/100*valor_compras)))
elif forma_pagamento == 2:
    print('O valor total é R${:.2f}, à vista no cartão tem 5% desconto.'.format(valor_compras-(5/100*valor_compras)))
elif forma_pagamento == 3:
        parcelas = int(input('Quantas parcelas? '))
        parcelas = valor_compras/2
        print('O valor total  da compra parcelado 2x no cartão é R${:.2f}'.format(valor_compras))
        print('Sua compra será parcelada em 2x de R${:.2f}.'.format(parcelas))
elif forma_pagamento == 4:
    parcelas = int(input('Quantas parcelas? '))
    valor_parcelado = (valor_compras + 20/100*valor_compras)
    print('Sua compra será parcelada em {:.2f}x de R${:.2f}.'.format(parcelas, valor_parcelado / parcelas))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(valor_compras, valor_parcelado))
else:
    print('Opção Inválida!')
