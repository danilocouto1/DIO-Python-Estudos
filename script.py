print(
    """Bem vindo ao banco DIO
        Qual operação deseja executar?
        """
)
section = -1
conta_global = 0


def depositar(deposito: int):
    global conta_global
    conta_global += deposito


def sacar(saque: int):
    global conta_global
    if saque > conta_global:
        print("Valor acima do permitido!")
    elif saque > 0:
        conta_global -= saque
        print("Saque efetuado com sucesso.")
    else:
        print("Valor invalido!")


while section != 0:
    section = input(
        """
        Digite:
        1 - Depositar
        2 - Sacar
        3 - Extrato
        0 - Fechar o programa
        """
    )

    if int(section) == 1:
        deposito = int(input("Quanto deseja depositar?\n"))
        depositar(deposito)
    elif int(section) == 2:
        saque = int(input("Quanto deseja sacar?\n"))
        sacar(saque)
    elif int(section) == 3:
        print(f"Valor em conta é: {conta_global}")
    elif int(section) == 0:
        print("Progama finalizado! Obrigado por usar serviços DIO.")
    else:
        print("Valor invalido! Digite Novamente.")
