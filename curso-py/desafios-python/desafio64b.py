# Flag para controlar quando o programa deve parar
flag = False  
# Contador para contar quantos números válidos foram digitados
cont = 0  
# Variável para armazenar a soma dos números digitados
soma = 0  

# Loop que continuará executando enquanto o flag for False
while not flag:
    # Solicita ao usuário que insira um número
    n = int(input('Digite um número [999 para parar]: '))
    
    # Verifica se o número digitado é o número de parada (999)
    if n == 999:
        # Zera a variável 'n' para não somar o número de parada
        n = 0  
        # Ativa o flag para encerrar o loop na próxima verificação
        flag = True  
    
    # Incrementa o contador (indica que um número foi digitado)
    cont += 1  
    # Soma o número digitado à variável 'soma'
    soma += n  

# Após o loop, exibe o total de números digitados (descontando o número de parada)
# e a soma dos números válidos
print('Você digitou {} números e a soma entre eles foi {}.'.format(cont - 1, soma))
