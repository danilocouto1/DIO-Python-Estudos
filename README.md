# 🏦 Banco DIO - DIO-Python-Estudos

Bem-vindo à branch **"Banco-Dio"** do repositório **"DIO-Python-Estudos"**, mantido por **Danilo Couto Pereira Santos**.

Este projeto faz parte do curso de **Python com foco em Inteligência Artificial e Análise de Dados**, oferecido pela **Digital Innovation One (DIO)**, e simula um sistema bancário mais completo, incluindo gerenciamento de usuários e contas.

---

## 🚀 Funcionalidades

O sistema bancário agora possui funcionalidades mais avançadas:

### 💰 Operações Bancárias

#### Depositar
- Permite adicionar saldo à conta.
- Apenas valores positivos são aceitos.
- Registra a operação no extrato.

#### Sacar
Permite realizar saques com as seguintes regras:
- Limite de **R$ 500 por saque**
- Máximo de **3 saques por execução**
- Não permite saque maior que o saldo disponível
- Registra a operação no extrato

#### Extrato
- Exibe todas as movimentações realizadas.
- Mostra o saldo atual formatado.
- Caso não haja movimentações, informa ao usuário.

---

### 👤 Gestão de Usuários

#### Criar Usuário
- CPF validado e formatado automaticamente (`###.###.###-##`)
- Data de nascimento validada (formato `dd-mm-aaaa`)
- Endereço validado no formato:
  ```
  cidade - UF
  ```
- Impede cadastro de CPF duplicado.

---

### 🏦 Gestão de Contas

#### Criar Conta
- Conta vinculada a um usuário existente.
- Agência padrão: `0001`
- Número da conta gerado automaticamente.

#### Listar Contas
- Exibe todas as contas cadastradas.

---

## 🛠️ Conceitos Aplicados no Código

Este projeto utiliza diversos conceitos importantes de Python:

- Funções com parâmetros posicionais (`/`)
- Funções com parâmetros nomeados obrigatórios (`*`)
- Manipulação de strings
- Expressões regulares (`re`)
- Manipulação de datas (`datetime`)
- Listas e dicionários
- Tratamento de exceções (`try/except`)
- Validação de dados
- Organização modular de código
- Boas práticas com `main()` e `if __name__ == "__main__"`

---

## ▶️ Como Executar

1. Clone o repositório:

```bash
git clone https://github.com/danilocouto1/DIO-Python-Estudos.git
```

2. Acesse a pasta do projeto:

```bash
cd DIO-Python-Estudos
```

3. Vá para a branch correta:

```bash
git checkout Banco-Dio
```

4. Execute o programa:

```bash
python nome_do_arquivo.py
```

---

## 📋 Menu do Sistema

Ao executar, o sistema exibirá:

```
Digite:
1 - Depositar
2 - Sacar
3 - Extrato
4 - Criar Usuário
5 - Criar Conta
6 - Listar Conta
0 - Fechar o programa
```

---

## 📌 Regras Importantes

- Limite por saque: **R$ 500**
- Máximo de saques: **3 por execução**
- Agência padrão: **0001**
- CPF deve conter 11 dígitos
- Data deve estar no formato: **dd-mm-aaaa**
- Endereço deve conter: **Cidade - UF**

---

## 📞 Contato

**Nome:** Danilo Couto Pereira Santos  
📱 Telefone: +55 (73) 9 8851-3272  
📧 E-mail: dansantos45@hotmail.com  
🔗 LinkedIn: https://www.linkedin.com/in/danilocoutopsantos/
