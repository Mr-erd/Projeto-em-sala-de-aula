# Sistema Bancário Simples 🏦

Este é um projeto simples de um sistema bancário desenvolvido em Python. Ele simula as operações básicas de uma conta corrente, como depósito, saque e visualização de extrato, tudo através de uma interface de linha de comando.

## 🎬 Demonstração em Ação

Veja abaixo uma simulação de como o programa funciona na prática:

```bash
====================================
Bem-vindo ao Sistema Bancário
====================================
[1]: Depositar
[2]: Sacar
[3]: Extrato
[4]: Sair
====================================
Escolha uma opção: 1
Digite o valor do depósito: 1500
Depósito realizado com sucesso! Saldo atual: R$ 1500.00
====================================
Bem-vindo ao Sistema Bancário
====================================
...
Escolha uma opção: 2
Digite o valor do saque: 300
Saque realizado com sucesso! Saldo atual: R$ 1200.00
====================================
Bem-vindo ao Sistema Bancário
====================================
...
Escolha uma opção: 3
Extrato:
Depósito: R$ 1500.00
Saque: R$ 300.00
Saldo atual: R$ 1200.00

Escolha uma opção: 4
Saindo do sistema. Até logo!
```

## ✨ Funcionalidades Principais

O sistema oferece as seguintes operações:

* **[1] Depositar 💰:** Permite ao usuário adicionar um valor positivo à sua conta.
* **[2] Sacar 💸:** Permite ao usuário retirar um valor da conta, sujeito a certas regras.
* **[3] Extrato 📄:** Exibe todas as transações realizadas (depósitos e saques) e o saldo final da conta.
* **[4] Sair 👋:** Encerra a execução do programa.

## 룰 Regras de Negócio

Para garantir a integridade da conta, o sistema implementa as seguintes regras na operação de saque:

* ✅ **Saldo Suficiente:** O usuário não pode sacar um valor maior do que o saldo disponível em conta.
* ✅ **Limite por Saque:** Cada saque não pode exceder o limite de **R$ 500,00**.
* ✅ **Limite de Quantidade:** O usuário pode realizar no máximo **3 saques**.

## 🛠️ Tecnologias Utilizadas

Este projeto foi construído utilizando apenas tecnologias nativas do:

* **Python 3**

## 🚀 Como Executar o Projeto

Para rodar este projeto em sua máquina local, siga os passos abaixo.

**Pré-requisitos:**
* Ter o [Python 3](https://www.python.org/downloads/) instalado.

**Passos:**

1.  Clone este repositório (ou simplesmente baixe o arquivo `.py`):
    ```bash
    git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
    ```

2.  Navegue até a pasta do projeto:
    ```bash
    cd seu-repositorio
    ```

3.  Execute o script Python:
    ```bash
    python nome_do_seu_arquivo.py
    ```
Pronto! O menu do sistema bancário aparecerá no seu terminal.

## 👨‍💻 Autor Eugenio Santana

Feito por **[Eugenio Santana]**.
