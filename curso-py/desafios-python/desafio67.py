while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    print('-'*35)
    for c in range(1, 11):
        print('{} x {:2} = {}'.format(num, c, num*c))
    if num < 0:
        break
    print('-'*35)
print('PROGRAMA TABUADA ENCERRADO.')