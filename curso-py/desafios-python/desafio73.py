times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio',
         'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
        'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia',
        'São Paulo', 'Fluminense', 'Sport Recife', 'EC Vitória',
        'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')
print('-='*15)
print(f'Lista de times: {times}')
print('-='*15)
print(f'Os 5 primeiros são {times[:5]}')
print('-='*15)
print(f'Times em ordem alfabética {sorted(times)}')
print('-='*15)
print(f'A Chapecoense está na posição {times.index('Chapecoense')}ª posição.')

#for t in times:
    #print(t)