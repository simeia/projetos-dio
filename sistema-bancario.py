
#depsito, saque, extrato
#aceita somente valores positivos no deposito
#nao precisa identificar conta e agencia, trabalha apenas com 1 usuario
#depositos devem ser armazenados em uma variavel e exibidos na operacao de extrato
#somente 3 saques diários
#limite maximo de saque 500


menu = """
    ***********MENU**********
    _________________________
    [1] Depositar dinheiro
    [2] Sacar dinheiros
    [3] Ver extrato bancário
    [4] Encerrar acesso
    _________________________
    *************************
"""

deposito = 0
saldo_total = 0
extrato = ""
opcao = -1
saques_realizados = 0
LIMITE_SAQUE = 3
LIMITE_SAQUE_VALOR = 500

while opcao != 0:
    opcao = int(input(menu))

    if opcao == 1:
        deposito = float(input("Digite o valor a ser depositado"))
        extrato += f"\nDepósito: R$ {deposito:.2f}"
        saldo_total += deposito
  
    elif opcao == 2:
        sacar = float(input("Digite o valor a ser sacado"))

        
        atingiu_limite_diario = saques_realizados >= LIMITE_SAQUE
        atingiu_limite_saque = sacar >= LIMITE_SAQUE_VALOR
        saldo_insuficiente = sacar > saldo_total

        if atingiu_limite_diario:
            print("Você não tem saldo suficiente")
        elif atingiu_limite_saque:
            print("Você já atingiu sei limite de saques diários, volte amanhã!")
        elif saldo_insuficiente:
            print("Seu limite de saque é de R$ 500,00")
        
        elif sacar > 0:
            saques_realizados += 1
            saldo_total -= sacar
            extrato += f"\nSaque: R$ {sacar:.2f}"
            print(f"Você sacou R$ {sacar:.2f} \nAgora seu saldo é: R$ {saldo_total:.2f}")
        else:
            print("Operacao falhou")

    elif opcao == 3:
        if extrato:
            print("\n================ EXTRATO ================")
            print(f"{extrato}\nSeu saldo total é: R$ {saldo_total:.2f}")
            print("==========================================")
        else:
            print("\n================ EXTRATO ================")
            print("Nenhuma movimentação foi realizada.")
            print("==========================================")

    elif opcao == 4:
        print("Obrigado por usar nosso super sistema bancário incrivelmente tecnológico!")
        break
    else:
        print("Sua opcao é invalida")