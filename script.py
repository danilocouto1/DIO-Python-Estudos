import re
from datetime import datetime


def depositar(saldo,valor, extrato, /):
    
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: \tR$: {valor:.2f}\n"
    else:
        print("Depósito falhou.")
    return saldo, extrato

def sacar(*, valor, saldo, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saque = numero_saques >= limite_saques
    if excedeu_saldo:
        print("Saque falhou! Saldo insuficiente.")
    elif excedeu_limite:
        print("Saque falhou! Valor do saque excede o limite.")
    elif excedeu_saque:
        print("Saque falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: \t\tR$: {valor:.2f}\n"
        numero_saques += 1
        print("Saque realizado com sucesso!")
    else:
        print("Saque falhou!")
    return saldo, extrato


def extrato_exibir(saldo, /, *, extrato):
    print("Extrato:")
    print("Sem movimentações!" if not extrato else extrato)
    print(f"Valor em conta é: R$: {saldo:.2f}")



def format_cpf(cpf_str):
    digits = re.sub(r"\D", "", cpf_str)
    if len(digits) != 11:
        raise ValueError("CPF deve conter 11 dígitos")
    return f"{digits[:3]}.{digits[3:6]}.{digits[6:9]}-{digits[9:]}"


def parse_date(date_str):
    try:
        return datetime.strptime(date_str, "%d-%m-%Y").date()
    except ValueError:
        raise ValueError("Data inválida. Use dd-mm-aaaa")


def validar_endereco(end_str):
    if "-" not in end_str:
        raise ValueError("Endereço precisa conter 'cidade - sigla'")
    cidade, estado = [p.strip() for p in end_str.split("-", 1)]
    estado = estado.upper()
    if len(estado) != 2 or not estado.isalpha():
        raise ValueError("Sigla do estado deve ter 2 letras")
    return f"{cidade}-{estado}"


def criar_usuario(users):
    while True:
        cpf_raw = input("Digite o CPF do usuário (somente números):\n")
        try:
            cpf = format_cpf(cpf_raw)
            break
        except ValueError as e:
            print(e)
    if filtrar_usuario(cpf, users):
        print("Já existe usuário com esse CPF!")
        return
    nome = input("Digite o nome do usuário:\n").strip()
    while True:
        try:
            data_nasc = parse_date(input("Digite a data de nascimento do usuário (dd-mm-aaaa):\n"))
            break
        except ValueError as e:
            print(e)
    while True:
        try:
            endereco = validar_endereco(input("Digite o endereço do usuário (cidade - sigla estado):\n"))
            break
        except ValueError as e:
            print(e)
    users.append({
        "nome": nome,
        "data_nascimento": data_nasc.strftime("%d-%m-%Y"),
        "cpf": cpf,
        "endereco": endereco,
    })
    print("Usuário criado com sucesso!")


def filtrar_usuario(cpf, user):
    try:
        cpf = format_cpf(cpf)
    except ValueError:
        return None
    user_filtrado = [usuario for usuario in user if usuario["cpf"] == cpf]
    return user_filtrado[0] if user_filtrado else None

def criar_conta(AGENCIA, numero_conta, *, users):
    cpf = input("Digite o CPF do usuário:\n")
    user = filtrar_usuario(cpf, users)
    if user:
        print("Conta criada com sucesso!")
        return {"Agencia": AGENCIA, "Numero Conta": numero_conta, "Usuario": user}
    print("Usuário não encontrado! Conta não criada.")


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    
    limite = 500
    saldo = 0
    extrato = ""
    numero_saques = 0
    users = []
    contas = []
    
    print("Bem-vindo ao banco DIO\nQual operação deseja executar?\n")
    while True:
        try:
            opcao = int(
                input(
                    """Digite:
                    1 - Depositar
                    2 - Sacar
                    3 - Extrato
                    4 - Criar Usuário
                    5 - Criar Conta
                    6 - Listar Conta
                    0 - Fechar o programa\n
                    """
                )
            )
            if opcao == 1:
                valor = int(input("Quanto deseja depositar?\n"))
                saldo, extrato = depositar(saldo, valor, extrato)
            elif opcao == 2:
                valor = int(input("Quanto deseja sacar?\n"))
                saldo, extrato = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)
            elif opcao == 3:
                extrato_exibir(saldo, extrato=extrato)
            elif opcao == 4:
               criar_usuario(users)
            elif opcao == 5:
                numero_conta = len(contas) + 1
                conta = criar_conta(AGENCIA, numero_conta, users=users)
                if conta:
                    contas.append(conta)
            elif opcao == 6:
                print([conta for conta in contas])
            elif opcao == 0:
                print("Programa finalizado! Obrigado por usar DIO.")
                break
            else:
                print("Opção inválida! Digite novamente.")
        except ValueError:
            print("Entrada inválida! Por favor, digite um número.")


if __name__ == "__main__":
    main()
