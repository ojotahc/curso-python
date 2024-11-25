# Desafio 57
sexo = str(input('Digite seu sexo [F/M]: ')).upper().strip()[0]
while sexo != 'M' and sexo != 'F':
  print('Valor inválido. Tente novamente!')
  sexo = str(input('Digite seu sexo [F/M]: ')).upper().strip()[0]
print('O seu sexo é {}'.format(sexo))
