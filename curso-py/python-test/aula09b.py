frase = 'Curso em Vídeo Python'
dividido = frase.split()
# FATIAMENTO
print(frase[3])
print(frase[3:13])
print(frase[:13])
print(frase[1:15:2])
print(frase[::2])

# Dica para escrever texto grande
print(""" Seu texto grandeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
      eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
      eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee""")

print(frase.count('o'))

# Posso juntar duas funções em uma - Função de Análise + Função de transformação
print(frase.upper().count('O'))

# ANÁLISE
print(len(frase))
print('Curso' in frase)
print(frase.find('Curso'))
print(frase.lower().find('vídeo'))

# TRANSFORMÇÃO
# Dica uma string ela é imutável. Mesmo eu usando essa função replace, o valor dá minha variável não vai mudar, só vai ser trocado no print
frase.replace('Python', 'Android')

# DIVISÃO
print(frase.split())
print(dividido[0])
print(dividido[2][3])
