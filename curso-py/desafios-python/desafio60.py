# Desafio 60

# Inicializamos a variável `f` com o valor 1.
# `f` será usada para armazenar o resultado do fatorial.
f = 1

# Solicitamos ao usuário que insira um número, que será armazenado em `n`.
n = int(input('Digite um número: '))

# Inicializamos o `contador` em 1.
# Esta variável será usada para contar de 1 até `n` no loop.
contador = 1

# Iniciamos o loop `while` que vai executar enquanto `contador` for menor ou igual a `n`.
while contador <= n:
    # Multiplicamos o valor atual de `f` pelo valor de `contador`.
    # Esse resultado é atribuído novamente a `f`, atualizando o valor acumulado do fatorial.
    f *= contador
    
    # Incrementamos `contador` em 1 para que ele vá avançando até `n`.
    contador += 1
    print(f)

# Após o loop terminar, `f` contém o fatorial de `n`.
# Imprimimos o valor final de `f`.
print(f)