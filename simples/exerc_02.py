#Escreva um programa para ler uma temperatura em graus Fahrenheit, 
# calcular e escrever o valor
#correspondente em graus Celsius. (C = (F-32) * 5 / 9)

Fahrenheit = float(input("Qual a temperatura em fahrenheit? "))
Celsius = (Fahrenheit-32)*5/9
print(Celsius)