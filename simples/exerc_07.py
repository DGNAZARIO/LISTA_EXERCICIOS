#A equipe Benneton-Ford deseja calcular o número mínimo de litros que deverá colocar no tanque de
#seu carro para que ele possa percorrer um determinado número de voltas até o primeiro
#reabastecimento. Escreva um programa que leia o comprimento da pista (em metros), o número total de
#voltas a serem percorridas no grande prêmio, o número de abastecimentos desejados e o consumo de
#combustível do carro (em Km/L). Calcular e escrever o número mínimo de litros necessários para
#percorrer até o primeiro reabastecimento. OBS: Considere que o número de voltas entre os
#abastecimentos é o mesmo.

comprimento = float(input("Comprimento da pista (em metros)?"))
voltas = int(input("Número total de voltas?"))
abastecimento = int(input("Número de abastecimentos desejados?"))
consumo = float(input("Consumo de combustível do carro (em Km/L)?"))

KmTotal = comprimento/1000 * voltas
consumoTotal = KmTotal / consumo
litros = consumoTotal / abastecimento

print("O numero minimo de litros necessario ate o primeiro reabastecimento:", litros)

