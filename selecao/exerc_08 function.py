from datetime import date

anoNasc = int(input("Qual o ano de seu nascimento?"))
ANOATUAL = date.today().year

resposta = ""
idade = ANOATUAL - anoNasc
if (idade > 16):
    resposta = "sim"

else:
    resposta = "não"

print("Voce poderá votar este ano: ", resposta)
print("Porque voce tem ", idade, "anos")
