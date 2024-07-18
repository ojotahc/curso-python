# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
preco = float(input('Digite o valor do produto: '))
desconto = float(preco * 0.05)
valorDesconto = float(preco - desconto)

# Outra forma - desconto = (preco * 5 / 100)

"""" 
Exemplo:
10*5/100
1500*10/100
875*15/100
"""

print('O valor com 5% desconto é {:.2f}'.format(valorDesconto))
