#Acrescente ao exercício anterior a mensagem Você foi REPROVADO! Estude mais... caso a
# média calculada seja menor que 6.0.

nota1 = float(input("Qual foi a sua primeira nota? "))
nota2 = float(input("Qual foi a sua segunda nota? "))
media = nota1 + nota2
if media >= 6.0:
    resposta1 = media
else:
    resposta2 = media 

print("Sua nota foi: ",media)
if media >= 6.0:
    print("PARABÉNS! Você foi aprovado!", resposta1)
else: 
    print("Você foi REPROVADO! Estude mais...", resposta2)
