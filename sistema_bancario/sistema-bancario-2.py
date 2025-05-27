import textwrap

menu = """
    ***********MENU**********
    _________________________
    [1] Depositar dinheiro
    [2] Sacar dinheiro
    [3] Ver extrato bancário
    [4] Cadastrar novo cliente
    [5] Criar nova conta
    [6] Ver todas as contas
    [0] Encerrar acesso
    _________________________
    *************************
"""

def exibir_menu():
    return int(input(textwrap.dedent(menu)))

def depositar(saldo_total, extrato):
    valor = float(input("Digite o valor a ser depositado: "))
    if valor > 0:
        saldo_total += valor
        extrato += f"\nDepósito: R$ {valor:.2f}"
        print("Depósito realizado com sucesso!")
    else:
        print("Valor inválido para depósito.")
    return saldo_total, extrato

def sacar(saldo_total, extrato, saques_realizados, LIMITE_SAQUE, LIMITE_SAQUE_VALOR):
    valor = float(input("Digite o valor a ser sacado: "))

    atingiu_limite_diario = saques_realizados >= LIMITE_SAQUE
    atingiu_limite_valor = valor > LIMITE_SAQUE_VALOR
    saldo_insuficiente = valor > saldo_total

    if atingiu_limite_diario:
        print("Você já atingiu seu limite de saques diários, volte amanhã!")
    elif atingiu_limite_valor:
        print("Seu limite de saque é de R$ 500,00")
    elif saldo_insuficiente:
        print("Você não tem saldo suficiente")
    elif valor > 0:
        saldo_total -= valor
        extrato += f"\nSaque: R$ {valor:.2f}"
        saques_realizados += 1
        print(f"Você sacou R$ {valor:.2f} \nAgora seu saldo é: R$ {saldo_total:.2f}")
    else:
        print("Operação falhou: valor inválido")

    return saldo_total, extrato, saques_realizados

def exibir_extrato(saldo_total, extrato):
    print("\n================ EXTRATO ================")
    if extrato:
        print(f"{extrato}\nSeu saldo total é: R$ {saldo_total:.2f}")
    else:
        print("Nenhuma movimentação foi realizada.")
    print("==========================================")

def cadastrar_cliente(clientes):
    cpf = input("Digite o CPF (apenas números): ")
    if cpf in [c["cpf"] for c in clientes]:
        print("Este CPF já está cadastrado.")
        return clientes
    nome = input("Nome completo: ")
    nascimento = input("Data de nascimento (dd-mm-aaaa): ")
    endereco = input("Endereço completo: ")
    clientes.append({"nome": nome, "cpf": cpf, "nascimento": nascimento, "endereco": endereco})
    print("Cliente cadastrado com sucesso!")
    return clientes

def criar_conta(contas, clientes):
    cpf = input("Informe o CPF do titular da conta: ")
    cliente = next((c for c in clientes if c["cpf"] == cpf), None)

    if not cliente:
        print("CPF não encontrado. Cadastre o cliente antes de criar a conta.")
        return contas

    numero = len(contas) + 1
    nova_conta = {"agencia": "0001", "numero": numero, "cliente": cliente}
    contas.append(nova_conta)

    print("Conta criada com sucesso!")
    print("=" * 40)
    print("Sua nova conta é:")
    print(f"Agência: {nova_conta['agencia']}")
    print(f"Conta: {nova_conta['numero']}")
    print(f"Titular: {nova_conta['cliente']['nome']}")

    return contas

def listar_contas(contas):
    if not contas:
        print("Nenhuma conta cadastrada.")
        return
    for conta in contas:
        print("=" * 40)
        print(f"Agência: {conta['agencia']}")
        print(f"Conta: {conta['numero']}")
        print(f"Titular: {conta['cliente']['nome']}")

saldo_total = 0
extrato = ""
saques_realizados = 0
LIMITE_SAQUE = 3
LIMITE_SAQUE_VALOR = 500
clientes = []
contas = []
opcao = -1

while opcao != 0:
    opcao = exibir_menu()

    if opcao == 1:
        saldo_total, extrato = depositar(saldo_total, extrato)

    elif opcao == 2:
        saldo_total, extrato, saques_realizados = sacar(
            saldo_total, extrato, saques_realizados, LIMITE_SAQUE, LIMITE_SAQUE_VALOR
        )

    elif opcao == 3:
        exibir_extrato(saldo_total, extrato)

    elif opcao == 4:
        clientes = cadastrar_cliente(clientes)

    elif opcao == 5:
        contas = criar_conta(contas, clientes)

    elif opcao == 6:
        listar_contas(contas)

    elif opcao == 0:
        print("Obrigado por usar nosso super sistema bancário incrivelmente tecnológico versão 2.0!")
        break

    else:
        print("Sua opção é inválida. Tente novamente.")