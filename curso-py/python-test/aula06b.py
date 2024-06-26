n1 = float(input('Digite um valor: '))
print(type(n1))

n2 = str(input('Digite um valor: '))
print(type(n2))

n3 = int(input('Digite um valor: '))
print(type(n3))

n4 = bool(input('Digite um valor: '))
print(type(n4))

# É um número?
n5 = (input('Digite um algo: '))
print(n5.isnumeric())

# É uma letra?
n6 = (input('Digite um algo: '))
print(n6.isalpha())

# É uma letra e um núemro?
n7 = (input('Digite um algo: '))
print(n7.isalnum())
