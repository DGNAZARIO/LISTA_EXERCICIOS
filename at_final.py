import random

def gerar_numeros_sorteados():
    return sorted(random.sample(range(1,61),6))

def obter_aposta_usuario():
    while True:
        try:
            aposta =set(map(int, input("Digite sua aposta (6 números distintos entre 1 e 60) separados por espaço: ").split()))
            if len(aposta) == 6 and all(1 <= num <= 60 for num in aposta):
                return sorted(aposta)
            else:print("Aposta inválida. Certifique-se de inserir 6 números distintos entre 1 e 60.")
        except ValueError:
            print("Entrada inválida. Certifique-se de inserir números inteiros separados por espaço.")

def verificar_acertos (sorteio, aposta):
    return len(set(sorteio) & set (aposta))
def main ():
    while True:
        sorteio = gerar_numeros_sorteados()
        print(f"Números sorteados: {sorteio}")

        aposta = obter_aposta_usuario()
        print(f"Sua aposta: {aposta}")

        acertos = verificar_acertos(sorteio, aposta)

        if acertos == 6:
            print("Parabéns! Você ganhou a Sena!")
        elif acertos == 5:
            print("Parabéns! Você ganhou a Quina!")
        elif acertos == 4:
            print("Parabéns! Você ganhou a Quadra!")
        else:
            print(f"Você acertou {acertos} números. Não ganhou prêmio desta vez.")
        resposta = input("Deseja realizar um novo sorteio? (s/n): ").strip().lower()
        if resposta != 's':
            print("Obrigado por jogar! Até a próxima.")
            break
if __name__ == "__main__":
    main()