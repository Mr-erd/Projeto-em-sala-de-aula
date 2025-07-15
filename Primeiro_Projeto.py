Menu = (
 "====================================",
    "Bem-vindo ao Sistema Bancário",
 "====================================",
    "[1]: Depositar",
    "[2]: Sacar",
    "[3]: Extrato",
    "[4]: Sair",
 "====================================",
)
saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

print("Bem-vindo(a)")
print("\n".join(Menu))

while True:


    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        deposito = float(input("Digite o valor do depósito: "))
        if deposito > 0:
            saldo += deposito
            extrato.append(f"Depósito: R$ {deposito:.2f}")
            print(f"Depósito realizado com sucesso! Saldo atual: R$ {saldo:.2f}")
            print("\n".join(Menu))
        else:
            print("Valor de depósito inválido.") 
            
    
    elif opcao == "2":
        saque = float(input("Digite o valor do saque: "))
        if saque > saldo:
            print("Saldo insuficiente para realizar o saque.")
        elif saque > limite:
            print(f"Valor do saque excede o limite de R$ {limite:.2f}.")
        elif numero_saques >= LIMITE_SAQUES:
            print(f"Limite de saques diários atingido ({LIMITE_SAQUES} saques).")
        elif saque <= 0:
            print("Valor de saque inválido.")
        else:
            saldo -= saque
            extrato.append(f"Saque: R$ {saque:.2f}")
            numero_saques += 1
            print(f"Saque realizado com sucesso! Saldo atual: R$ {saldo:.2f}")
            print("\n".join(Menu))
            
    elif opcao == "3":
        if not extrato:
            print("================================================")
            print("Não foram realizadas movimentações.")
            print("Saldo atual: R$ 0.00")
            print("================================================")
        else:
            print("\n ============Extrato================"),
        
            for movimento in extrato:
                print(movimento)
            print(f"Saldo atual: R$ {saldo:.2f}")
            print("\n ====================================")

    elif opcao == "4":
        print("Saindo do sistema. Até logo!")
        break