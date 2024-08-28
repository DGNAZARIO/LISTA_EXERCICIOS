#Faça um algoritmo que conte de 1 a 100 e a 
# cada múltiplo de 10 emita uma mensagem:
#“Múltiplo de 10”.

multiplo = int(input("Qual seria o multiplo?"))
valorInicial = int(input("Qual seria o valor inicial?")) #100
valorFinal = int(input("Qual seria o valor final?")) #1

if(valorFinal < valorFinal):
    for i in range(valorInicial, valorFinal+1): # 101
        if(i % multiplo == 0):
            print(i, " multiplo ", multiplo)
        else:
            print(i)
else:
    print("Valor de entrada invalidos!")
