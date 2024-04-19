conta_global = 0


def depositar(valor):
    global conta_global
    if valor > 0:
        conta_global += valor
        print("Depósito efetuado com sucesso.")
    else:
        print("Valor inválido para depósito!")


def sacar(valor):
    global conta_global
    if valor > conta_global:
        print("Valor acima do permitido!")
    elif valor > 0:
        conta_global -= valor
        print("Saque efetuado com sucesso.")
    else:
        print("Valor inválido para saque!")


def extrato():
    global conta_global
    print(f"Valor em conta é: {conta_global}")


def main():
    print("Bem-vindo ao banco DIO\nQual operação deseja executar?\n")
    while True:
        try:
            opcao = int(
                input(
                    """Digite:
                    1 - Depositar
                    2 - Sacar
                    3 - Extrato
                    0 - Fechar o programa\n
                    """
                )
            )
            if opcao == 1:
                valor = int(input("Quanto deseja depositar?\n"))
                depositar(valor)
            elif opcao == 2:
                valor = int(input("Quanto deseja sacar?\n"))
                sacar(valor)
            elif opcao == 3:
                extrato()
            elif opcao == 0:
                print("Programa finalizado! Obrigado por usar DIO.")
                break
            else:
                print("Opção inválida! Digite novamente.")
        except ValueError:
            print("Entrada inválida! Por favor, digite um número.")


if __name__ == "__main__":
    main()
