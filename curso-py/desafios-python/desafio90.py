dados_aluno = dict()

dados_aluno['nome'] = str(input('Digite o nome do aluno: '))
dados_aluno['media'] = float(input('Digite a média do aluno: ')) 
if dados_aluno['media'] < 5:
    print(f'- Nome é igual a {dados_aluno["nome"]}')
    print(f'- Média é igual a {dados_aluno["media"]}')
    print('- Situação é igual a Reprovado')

elif dados_aluno['media'] < 7:
    print(f'- Nome é igual a {dados_aluno["nome"]}')
    print(f'- Média é igual a {dados_aluno["media"]}')
    print('- Situação é igual a Recuperação')

else:
    print(f'- Nome é igual a {dados_aluno["nome"]}')
    print(f'- Média é igual a {dados_aluno["media"]}')
    print('- Situação é igual a Aprovado')