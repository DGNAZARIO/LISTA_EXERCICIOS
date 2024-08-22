# As maçãs custam R$ 0,30 cada se forem compradas menos do que uma dúzia, e R$ 0,25 se forem
#compradas pelo menos doze. Escreva um programa que leia o número de maçãs compradas, calcule e
#escreva o valor total da compra.

maca = int(input("Quantas maças vc comprou? "))
maca1 = maca * 0.30
maca2 = maca * 0.25

if maca >= 12:
    resposta1 = maca1

else:
    resposta2 = maca2


if maca:
    print("Voce comprou ",maca, "maças a ", resposta1, "total e cada uma saiu a 0.25 centavos.")

else:
    print("Voce comprou ",maca, "maças a", resposta2, "total e cada uma saiu a 0.30 centavos" )