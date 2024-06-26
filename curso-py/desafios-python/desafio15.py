dias = int(input('Quantos dias o carro foi   alugado?: '))
km = float(input('Quantos Km o carro rodou?: '))
total = float((dias * 60) + (km * 0.15))
print('Você alugou o carro por {} dias e rodou {:.0f} km, portanto o preço total é R${:.2f}'.format(
    dias, km, total))
