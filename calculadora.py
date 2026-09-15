"""
Calculadora simples em Python
------------------------------
Objetivo: praticar funções, tratamento de erros e loops.
"""

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ValueError("Não é possível dividir por zero!")
    return a / b


def pegar_numero(mensagem):
    """Fica pedindo um número até o usuário digitar algo válido."""
    while True:
        valor = input(mensagem)
        try:
            return float(valor)
        except ValueError:
            print("Isso não é um número válido. Tente de novo.")


def menu():
    print("\n===== CALCULADORA =====")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("0 - Sair")


def main():
    operacoes = {
        "1": ("Soma", somar),
        "2": ("Subtração", subtrair),
        "3": ("Multiplicação", multiplicar),
        "4": ("Divisão", dividir),
    }

    while True:
        menu()
        escolha = input("Escolha uma opção: ").strip()

        if escolha == "0":
            print("Até mais!")
            break

        if escolha not in operacoes:
            print("Opção inválida, tente novamente.")
            continue

        nome, funcao = operacoes[escolha]
        a = pegar_numero("Digite o primeiro número: ")
        b = pegar_numero("Digite o segundo número: ")

        try:
            resultado = funcao(a, b)
            print(f"\n{nome}: {a} e {b} => Resultado: {resultado}")
        except ValueError as erro:
            print(f"Erro: {erro}")


if __name__ == "__main__":
    main()
