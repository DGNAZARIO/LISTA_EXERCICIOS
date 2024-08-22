#Escreva um programa para ler as notas das duas avaliações de um aluno no semestre, calcular e
#escrever a média semestral e a seguinte mensagem: PARABÉNS! Você foi aprovado! somente se o
#aluno foi aprovado (considere 6.0 a média mínima para aprovação).

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
    print("Que pena, Voce foi reprovado!", resposta2)