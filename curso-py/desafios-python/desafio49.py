num = int(input('Digite um número: '))
# a variável c que muda constantemente
for c in range(1, 11):
    print('{} x {:2} = {}'.format(num, c, num*c))
