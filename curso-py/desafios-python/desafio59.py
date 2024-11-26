opcao = 0
num = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

while opcao != 5:
  print('-='*10)
  print('[1] Somar')
  print('[2] Multiplicar')
  print('[3] Maior')
  print('[4] Novos Número')
  print('[5] Sair do Programa')
  print('-='*10)

  opcao = int(input('Qual é a sua opção? '))
  if opcao == 1:
    soma = num + num2
    print('A soma entre {} e {} é {}.'.format(num, num2, soma))
  elif opcao == 2:
    mult = num * num2
    print('A multiplicação entre {} e {} é {}.'.format(num, num2, mult))
  elif opcao == 3:
    if num > num2:
      print('Entre {} e {} o {} é maior.'.format(num, num2, num))
    else:
      print('Entre {} e {} o {} é maior.'.format(num, num2, num2))
  elif opcao == 4:
    num = int(input('Digite um número: '))
    num2 = int(input('Digite outro número: '))
  elif opcao == 5:
    print('Finalizando...')
  else:
    print('Opção inválida, tente novamente!')  
print('\n')
print('O programa terminou!')