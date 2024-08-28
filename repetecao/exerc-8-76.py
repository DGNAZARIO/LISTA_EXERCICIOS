#76) Construa um algoritmo que leia 50 valores inteiros e positivos e:
#· Encontre o maior valor
#· Encontre o menor valor
#· Calcule a média dos números lidos
#OBS1. Refaça o exercícios ussando lista para armazenaros valores digitados pelo usuario.
#OBS2. Faça com que o sistema soteie 6 valores digitados pelo usuarios logo após o exibir as mensagens (random.randrange(1, 51))

maior = 0
menor = 0
soma = 0

for x in range(1, 6):
    valor = int(input(f"Qual o {x}º valor?"))