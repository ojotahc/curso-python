"""
Faça um programa que peça uma nota, entre zero e dez. 
Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido. 

"""


for tentativa in range(5):  # Define um número máximo de 5 tentativas
    nota = int(input("Digite uma nota entre 0 e 10: "))
    if 0 <= nota <= 10:
        print(f"A nota foi {nota}.")
        break  # Sai do loop se a nota for válida
    else:
        print("Valor inválido. Tente novamente.")

# Se o loop terminar sem receber uma nota válida, exibe uma mensagem
else:
    print("Número máximo de tentativas alcançado. Programa encerrado.")
