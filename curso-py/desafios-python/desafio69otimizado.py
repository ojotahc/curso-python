# Inicialização das variáveis para contagem
total_pessoas_maior = 0
total_homens = 0
total_mulheres_vinte_anos = 0

# Loop principal para cadastro de várias pessoas
while True:
    print('-'*20)
    print('CADASTRE UMA PESSOA')
    print('-'*20)
    
    # Leitura e validação da idade
    idade = int(input('Idade: '))
    
    # Contagem de pessoas com mais de 18 anos
    if idade > 18:
        total_pessoas_maior += 1
    
    # Leitura e validação do sexo
    sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    
    # Validação do sexo para garantir que seja 'M' ou 'F'
    while sexo not in ['M', 'F']:
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    
    # Contagem dos homens cadastrados
    if sexo == 'M':
        total_homens += 1
    
    # Contagem de mulheres com menos de 20 anos
    if idade < 20 and sexo == 'F':
        total_mulheres_vinte_anos += 1

    # Pergunta se o usuário quer continuar cadastrando mais pessoas
    escolha = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    
    # Validação da resposta para continuar ou encerrar o cadastro
    while escolha not in ['S', 'N']:
        escolha = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    
    # Se a resposta for 'N', encerra o loop
    if escolha == 'N':
        break

# Exibição dos resultados
print('===== FIM DO PROGRAMA =====')
print(f'Total de pessoas com mais de 18 anos: {total_pessoas_maior}')
print(f'Ao total temos {total_homens} homem(ens) cadastrados.')
print(f'Ao total temos {total_mulheres_vinte_anos} mulher(es) com menos de 20 anos.')
