n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
sub = n1 - n2

# print('A soma vale {}'.format(n1+n2)) - Forma alternativa, pois nesse caso eu não preciso da variável soma.
print('A some é {}'.format(s))

print('A multiplicação é {}'.format(m))

print('A divisão é {}'.format(d))

print('A divisão inteira é {}'.format(di))

print('A potência é {}'.format(e))

print('A diferença á {}'.format(sub))

# \n serve para quebrar a linha e o end para juntar o print com outro print
print('A some é {}, \n o produto é {}, e a divisão é {:.3f}'.format(s, m, d), end=' ')
print('A divisão inteira é {}, e a potência é {}'.format(di, e))
