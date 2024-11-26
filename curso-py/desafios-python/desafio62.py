primeiro = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
termo = primeiro
contador = 1
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while contador <= total:
        print(termo, end=' -> ')
        contador += 1
        termo += r
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))