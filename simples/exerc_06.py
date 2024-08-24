#Declaração mais simples: Faça um programa que calcule a renda diária de 
# #um motorista de táxi. O usuário deve informar a quilometragem rodada, 
# #o consumo de combustível e a receita obtida, e o programa deve calcular 
# o consumo médio e o lucro líquido.

#Faça um programa que calcule a renda diária de um motorista 
# de táxi. O usuário deve informar a quilometragem rodada, o 
# consumo de combustível e a receita obtida, e o programa deve 
# calcular o consumo médio e o lucro líquido.

km_inicial = float(input("odômetro (Km) no inicio do dia? "))
km_final = float(input("odômetro (Km) no final do dia? "))
abastecimento = float(input("Quantos litros de gasolina vc abasteceu? "))
Recebido = float(input("Qual foi a receita obtida hoje? "))
GASOLINA = 4.87 


km_rodado = km_inicial / km_final
consumo_por_litro = km_rodado / abastecimento
consumo_medio = consumo_por_litro * GASOLINA
lucro = Recebido / consumo_medio
print(consumo_medio)
print(lucro)


# Dicionário para armazenar viagens
viagens = []

def registrar_viagem(data, distancia, valor):
    """Registra uma nova viagem."""
    viagem = {
        'data': data,
        'distancia': distancia,
        'valor': valor
    }
    viagens.append(viagem)
    print(f"Viagem registrada: {viagem}")

def calcular_rendimento_diario(data):
    """Calcula o rendimento total em um dia específico."""
    rendimento = sum(viagem['valor'] for viagem in viagens if viagem['data'] == data)
    return rendimento

def gerar_relatorio(periodo_inicio, periodo_fim):
    """Gera um relatório de rendimentos em um intervalo de datas."""
    rendimento_total = sum(
        viagem['valor']
        for viagem in viagens
        if periodo_inicio <= viagem['data'] <= periodo_fim
    )
    return rendimento_total

def main():
    while True:
        print("\nMenu:")
        print("1. Registrar Viagem")
        print("2. Calcular Rendimento Diário")
        print("3. Gerar Relatório")
        print("4. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == "1":
            data_str = input("Digite a data da viagem (YYYY-MM-DD): ")
            data = datetime.datetime.strptime(data_str, "%Y-%m-%d").date()
            distancia = float(input("Digite a distância da viagem (em km): "))
            valor = float(input("Digite o valor cobrado (em R$): "))
            registrar_viagem(data, distancia, valor)
        
        elif escolha == "2":
            data_str = input("Digite a data (YYYY-MM-DD) para calcular o rendimento: ")
            data = datetime.datetime.strptime(data_str, "%Y-%m-%d").date()
            rendimento = calcular_rendimento_diario(data)
            print(f"O rendimento em {data} foi R${rendimento:.2f}")
        
        elif escolha == "3":
            inicio_str = input("Digite a data de início (YYYY-MM-DD): ")
            fim_str = input("Digite a data de fim (YYYY-MM-DD): ")
            periodo_inicio = datetime.datetime.strptime(inicio_str, "%Y-%m-%d").date()
            periodo_fim = datetime.datetime.strptime(fim_str, "%Y-%m-%d").date()
            rendimento_total = gerar_relatorio(periodo_inicio, periodo_fim)
            print(f"O rendimento total de {periodo_inicio} a {periodo_fim} foi R${rendimento_total:.2f}")
        
        elif escolha == "4":
            print("Saindo do aplicativo...")
            break
        
        else:
            print("Opção inválida. Por favor, escolha novamente.")

if __name__ == "__main__":
    main()


