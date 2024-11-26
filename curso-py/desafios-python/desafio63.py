# F(n)=F(n−1)+F(n−2)
t1 = 0
t2 = 1

cont = 3

n = int(input('Quantos termos você quer mostrar? '))
print('{} -> {}'.format(t1, t2), end='')

while cont <= n:
    t3 = t1 + t2
    print(' -> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1









