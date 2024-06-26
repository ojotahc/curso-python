largura = float(input('Digite a largura da parede em metros:'))
altura = float(input('Digite a altura da parede em metros: '))
area = float(largura * altura)
tinta = float(area / 2)

print('A sua parede tem {} metros quadrados, você precisade {} litros de tinta para pintá-la.'.format(area, tinta))
