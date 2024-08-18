#Escreva um programa que calcule o número de lâmpadas necessárias 
# para iluminar uma sala. O usuário deve informar as dimensões da 
# sala e a potência de cada lâmpada, e o programa deve indicar quantas lâmpadas são necessárias.

comprimento1 = float(input("Qual o comprimento em metros? "))
largura1 = float(input("Qual a largura em metros? "))
altura1 = float(input("Qual a altura em metros? "))
lampada1 = float(input("Qual a potência da lâmpada? "))

sala1 = comprimento1 * largura1 * altura1
iluminacao_base1 = 300
iluminacao_necessaria = lampada1 / iluminacao_base1
total1 = sala1, iluminacao_necessaria
print("o numero total de lampaas é: ",total1) 


def calcular_area(comprimento, largura):
    """Calcula a área do cômodo."""
    return comprimento * largura

def calcular_volume(comprimento, largura, altura):
    """Calcula o volume do cômodo."""
    return comprimento * largura * altura

def fator_cor(cor):
    """Retorna um fator de correção baseado na cor das paredes."""
    if cor.lower() == 'claro':
        return 1.0
    elif cor.lower() == 'escuro':
        return 1.5
    else:
        raise ValueError("Cor inválida. Use 'claro' ou 'escuro'.")

def fator_atividade(atividade):
    """Retorna um fator de correção baseado na atividade realizada."""
    if atividade.lower() == 'baixa':
        return 1.0
    elif atividade.lower() == 'média':
        return 1.5
    elif atividade.lower() == 'alta':
        return 2.0
    else:
        raise ValueError("Atividade inválida. Use 'baixa', 'média' ou 'alta'.")

def calcular_lampadas_necessarias(comprimento, largura, altura, potencia_lampada, cor, atividade):
    """
    Calcula o número de lâmpadas necessárias e a potência total recomendada para o cômodo.
    
    :param comprimento: Comprimento do cômodo em metros.
    :param largura: Largura do cômodo em metros.
    :param altura: Altura do teto em metros.
    :param potencia_lampada: Potência de cada lâmpada em watts.
    :param cor: Cor das paredes ('claro' ou 'escuro').
    :param atividade: Tipo de atividade realizada ('baixa', 'média', 'alta').
    :return: Número de lâmpadas necessárias e potência total recomendada.
    """
    area = calcular_area(comprimento, largura)
    
    # Fatores de correção
    fator_cor_ajustado = fator_cor(cor)
    fator_atividade_ajustado = fator_atividade(atividade)
    
    # Iluminação recomendada em lúmens por metro quadrado
    iluminacao_base = 300  # Valor típico de lúmens por metro quadrado para ambientes gerais
    iluminacao_necessaria = area * iluminacao_base * fator_cor_ajustado * fator_atividade_ajustado
    
    # Assumindo que cada watt de potência de lâmpada fornece aproximadamente 10 lúmens
    lumens_por_lampada = potencia_lampada * 10
    num_lampadas = iluminacao_necessaria / lumens_por_lampada
    
    # Arredondar para cima para garantir que a iluminação será suficiente
    num_lampadas = int(-(-num_lampadas // 1))  # Alternativa ao math.ceil()
    
    return num_lampadas, potencia_lampada * num_lampadas

def main():
    print("Bem-vindo ao Calculador de Iluminação para Cômodos!")
    
    try:
        # Entrada do usuário
        comprimento = float(input("Digite o comprimento do cômodo em metros: "))
        largura = float(input("Digite a largura do cômodo em metros: "))
        altura = float(input("Digite a altura do teto em metros: "))
        potencia_lampada = float(input("Digite a potência de cada lâmpada em watts: "))
        cor = input("Digite a cor das paredes (claro ou escuro): ")
        atividade = input("Digite o tipo de atividade realizada (baixa, média, alta): ")
        
        # Cálculo do número de lâmpadas e potência total
        num_lampadas, potencia_total = calcular_lampadas_necessarias(comprimento, largura, altura, potencia_lampada, cor, atividade)
        
        # Exibição do resultado
        print(f"\nPara iluminar o cômodo com as seguintes características:")
        print(f"- Comprimento: {comprimento} metros")
        print(f"- Largura: {largura} metros")
        print(f"- Altura do teto: {altura} metros")
        print(f"- Potência de cada lâmpada: {potencia_lampada} watts")
        print(f"- Cor das paredes: {cor}")
        print(f"- Tipo de atividade: {atividade}")
        print(f"\nVocê precisará de {num_lampadas} lâmpadas de {potencia_lampada} watts cada.")
        print(f"A potência total recomendada é {potencia_total} watts.")
    
    except ValueError as e:
        print(f"Erro: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")

if __name__ == "__main__":
    main()
