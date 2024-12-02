total_pessoas_maior = 0
total_homens = 0
total_mulheres_vinte_anos = 0
while True:
    print('-'*20)
    print('CADASTRE UMA PESSOA')
    print('-'*20)
    idade = int(input('Idade: '))
    if idade > 18:
        total_pessoas_maior += 1
    sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if sexo == 'M':
        total_homens += 1
    if idade < 20 and sexo == 'F':
        total_mulheres_vinte_anos += 1
    while sexo != 'M' and sexo != 'F':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    escolha = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    while escolha != 'S' and escolha != 'N':
        escolha = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if escolha == 'N':
        break
print('===== FIM DO PROGRAMA =====')
print(f'Total de pessoas com mais de 18 anos: {total_pessoas_maior}')
print(f'Ao total temos {total_homens} homem(ens) cadastrados.')
print(f'Ao total temos {total_mulheres_vinte_anos} mulher(es) com menos de 20 anos.')
