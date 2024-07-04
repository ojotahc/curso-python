valor_Casa = float(input('Digite o valor da casa: R$'))
salario_Comprador = float(input('Digite o valor do seu salário: R$'))
anos_Pagamento = int(input('Digite em quantos anos deseja pagar: ')) 
prestacao_Mensal = valor_Casa / (anos_Pagamento * 12)
   
if prestacao_Mensal <= salario_Comprador * 0.30:
    print('EMPRÉSTIMO APROVADO!!!')
elif prestacao_Mensal > salario_Comprador * 0.30:
    print('Infelizmente você não pode financiar essa casa.')
print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}.'.format(valor_Casa, anos_Pagamento, prestacao_Mensal))

"""
Versão Guanabara

casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100

print - para mostrar ao usuário
"""