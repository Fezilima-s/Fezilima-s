Menu = """    

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """    # Variável com linhas múltiplas

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3      # Variáveis para sistema funcionar

while True: # Condição com loop

    opcao = input(Menu) 

    if opcao == "1":
        valor = float(input("Informe o valor que deseja depositar: "))

        if valor > 0: # O valor não pode ser negativo ou igual a 0
            saldo += valor 
            extrato += f"Depósito: R$ {valor:.2f}\n" # Para registrar operação

        else:
            print("Operação falhou! Você deve depositar um valor a partir de R$1,00.")

    elif opcao == "2":
        valor = float(input("Informe o valor que deseja sacar: "))

        excedeu_saldo = valor > saldo # Quando saldo é insuficiente

        excedeu_limite = valor > limite # Quando valor é maior que R$500,00

        excedeu_saques = numero_saques >= LIMITE_SAQUES # A partir da 4ª tentativa de saque no dia

        if excedeu_saldo:
            print("Operação falhou! Você não possui saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O limite de saque é de R$500,00.")

        elif excedeu_saques:
            print("Operação falhou! Só é possível sacar três vezes por dia .")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n" # Para registrar no extrato
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "3":
        print("\n|=============== EXTRATO ===============|")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("|=======================================|")

    elif opcao == "0":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
