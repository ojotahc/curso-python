n =1
while n != 0:
  n = int(input('Digite um valor: '))
print('Fim')


r = 'S'
while r == 'S':
  r = str(input('Quer continuar? [S/N] ')).upper()
print('Fim')

n = 1
par = 0
impar = 0
while n != 0:
  n = int(input('Digite um valor: '))
  if n != 0:
    if n % 2 == 0:
      par += 1
    else:
      impar += 1
print(par)
print(impar)