from num2words import num2words

# Convertendo um número para texto em português
numero = 123
texto = num2words(numero, lang='pt_BR')

print(texto)  # saída: "cento e vinte e três"
