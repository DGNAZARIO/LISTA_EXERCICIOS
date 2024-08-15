#Escreva um programa para ler um valor e escrever se é 
# positivo ou negativo. Considere o valo zero como positivo

valor = int(input("Escreva um valor:"))

resposta = ""
if valor >= 0:
    resposta = "Positivo"

else :
    resposta = "Negativo"

print ("O valor é", resposta)

