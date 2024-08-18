#Escreva um programa para ler as dimensões de uma cozinha retangular (comprimento, largura e
#altura), calcular e escrever a quantidade de caixas de azulejos para se colocar em todas as suas
#paredes (considere que não será descontada a área ocupada por portas e janelas). Cada caixa de
#azulejos possui 1,5 m2.

Comprimento = float(input("Qual o comprimento da cozinha? "))
Largura = float(input("Qual a largura da cozinha? "))
Altura = float(input("Qual a altura da cozinha? "))
Azulejo = ((Comprimento*Altura)+(Largura*Altura))/1.5
print("A quantidade de caixas de azulejos necessaria é:", Azulejo)

def calcular_custo_ladrilhos(tipo_ladrilho, area):
    preços = {
        'porcelanato': 60.00,  # preço por metro quadrado
        'cerâmica': 40.00,
        'mármore': 100.00
    }
    if tipo_ladrilho not in preços:
        raise ValueError("Tipo de ladrilho não reconhecido.")
    custo_por_metro = preços[tipo_ladrilho]
    return custo_por_metro * area

def calcular_custo_acabamento(tipo_acabamento, area):
    preços = {
        'glossy': 20.00,  # preço por metro quadrado
        'mate': 15.00,
        'texturizado': 25.00
    }
    if tipo_acabamento not in preços:
        raise ValueError("Tipo de acabamento não reconhecido.")
    custo_por_metro = preços[tipo_acabamento]
    return custo_por_metro * area

def calcular_custo_mao_obra(area):
    custo_por_metro = 50.00  # preço por metro quadrado
    return custo_por_metro * area

def calcular_custo_outros_materiais():
    materiais = {
        'cola': 30.00,
        'rejunte': 25.00,
        'ferramentas': 40.00
    }
    return sum(materiais.values())

def gerar_orcamento():
    print("Bem-vindo ao Gerador de Orçamento para Reforma de Cozinha!")

    try:
        area = float(input("Digite a área da cozinha em metros quadrados: "))
        if area <= 0:
            raise ValueError("A área deve ser um número positivo.")

        tipo_ladrilho = input("Escolha o tipo de ladrilho (porcelanato, cerâmica, mármore): ").lower()
        tipo_acabamento = input("Escolha o tipo de acabamento (glossy, mate, texturizado): ").lower()

        custo_ladrilhos = calcular_custo_ladrilhos(tipo_ladrilho, area)
        custo_acabamento = calcular_custo_acabamento(tipo_acabamento, area)
        custo_mao_obra = calcular_custo_mao_obra(area)
        custo_outros = calcular_custo_outros_materiais()

        custo_total = custo_ladrilhos + custo_acabamento + custo_mao_obra + custo_outros

        print("\nResumo do Orçamento:")
        print(f"Custo de Ladrilhos ({tipo_ladrilho}): R$ {custo_ladrilhos:.2f}")
        print(f"Custo de Acabamento ({tipo_acabamento}): R$ {custo_acabamento:.2f}")
        print(f"Custo de Mão de Obra: R$ {custo_mao_obra:.2f}")
        print(f"Custo de Outros Materiais: R$ {custo_outros:.2f}")
        print(f"\nCusto Total: R$ {custo_total:.2f}")

    except ValueError as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    gerar_orcamento()
