#Um motorista de táxi deseja calcular o rendimento de seu carro na praça. Sabendo-se que o preço do
#combustível é de R$ 4,87, escreva um programa para ler: a marcação do odômetro (Km) no início do
#dia, a marcação (Km) no final do dia, o número de litros de combustível gasto e o valor total (R$)
#recebido dos passageiros. Calcular e escrever: a média do consumo em Km/L e o lucro (líquido) do dia.

km_inicial = int(input("odômetro (Km) no início do dia?"))
km_final = int(input("odômetro (Km) no final do dia?"))
abastecimento = int(input("Número de abastecimentos desejados?"))
Recebido = int(input("Qual foi a media por passageiro recebida?"))
gasolina = 4,87 

km_rodado = km_inicial-km_final
Valor = km_rodado/Recebido
Gastos = abastecimento*gasolina
Lucro = Valor-Gastos
Media_consumo = km_rodado-Gastos
print(Media_consumo)
print(Lucro)