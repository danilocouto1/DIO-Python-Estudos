# Banco Dio - DIO-Python-Estudos

Bem-vindo à branch "Banco-Dio" do repositório "DIO-Python-Estudos", mantido por Danilo Couto Pereira Santos. Esta branch é dedicada a um projeto de simulação de operações bancárias, como parte das atividades do curso de Python focado em Inteligência Artificial e análise de dados oferecido pela Digital Innovation One (DIO).

## Funcionalidades

Este programa simula um sistema bancário simples, permitindo ao usuário realizar operações como:

- **Depositar**: Adiciona dinheiro à conta.
- **Sacar**: Retira dinheiro da conta, se houver saldo suficiente.
- **Extrato**: Mostra o saldo atual.
- **Fechar o Programa**: Encerra a execução do programa.

## Como Usar

Para executar o programa dentro desta branch, siga os passos abaixo:

1. Clone o repositório DIO-Python-Estudos e navegue para esta branch:

```bash
git clone https://github.com/danilocouto1/DIO-Python-Estudos.git
cd DIO-Python-Estudos
git checkout Banco-Dio
```

2. Execute o programa no terminal ou em um ambiente de desenvolvimento Python.

## Código Principal

```python
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
    else:
        conta_global -= saque
        print("Saque efetuado com sucesso.")

while section != 0:
    section = int(
        input(
            """
        Digite:
        1 - Depositar
        2 - Sacar
        3 - Extrato
        0 - Fechar o programa
        """
        )
    )
    if section == 1:
        deposito = int(input("Quanto deseja depositar?\n"))
        depositar(deposito)
    elif section == 2:
        saque = int(input("Quanto deseja sacar?\n"))
        sacar(saque)
    elif section == 3:
        print(f"Valor em conta é: {conta_global}")
    elif section == 0:
        print("Programa finalizado! Obrigado por usar os serviços DIO.")
    else:
        print("Valor inválido! Digite novamente.")
```

## Contato

- **Nome:** Danilo Couto Pereira Santos
- **Telefone:** +55 (73) 9 8851-3272
- **E-mail:** [dansantos45@hotmail.com](mailto:dansantos45@hotmail.com)
- **LinkedIn:** [Danilo Couto Pereira Santos](https://www.linkedin.com/in/danilocoutopsantos/)
