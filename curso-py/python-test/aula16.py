# Tuplas - variável que guarda mais de um valor
# Tuplas são imutáveis

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')

print(lanche[0])

print(len(lanche))

for comida in lanche:
    print(comida)

for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')

for cont in range(0, len(lanche)):
    print(cont)

# se eu precisar usar a posição eu faço dessa maneira
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

# posso fazer dessa maneira tbm
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')