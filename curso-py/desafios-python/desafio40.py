"""
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO
"""
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2

# if 7 > media >= 5 - Outra forma de pensar
if media < 5.0:
    print('REPROVADO!')
elif media >= 5 and media <= 7:
    print('RECUPEREÇÃO!') 
else:
    print('APROVADO!')
print('Tirando {} e {}, a média do aluno é {:.1f}.'.format(nota1, nota2, media))