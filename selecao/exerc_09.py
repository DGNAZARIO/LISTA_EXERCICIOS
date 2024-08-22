# As maçãs custam R$ 0,30 cada se forem compradas menos do que uma dúzia, e R$ 0,25 se forem
#compradas pelo menos doze. Escreva um programa que leia o número de maçãs compradas, calcule e
#escreva o valor total da compra.

maca = int(input("Quantas maças vc comprou? "))
maca1 = maca * 0.30
maca2 = maca * 0.25

if maca >= 12:
    resposta = maca2

else:
    resposta = maca1

print("Voce comprou ",maca, "maças a R$",resposta)