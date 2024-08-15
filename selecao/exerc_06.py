#Reescreva o programa do exercício anterior considerando o zero como neutro, ou seja, se for
#digitado o valor zero, escrever a palavra zero

valor = int(input("Escreva um valor:"))

resposta = ""
if valor == 0:
    resposta = "Zero"

elif valor > 0:
    resposta = "Positivo"

else :
    resposta = "Negativo"


print ("O valor é", resposta)

