def menu():
    menu = """

        [1] - Depositar
        [2] - Sacar
        [3] - Extrato
        [4] - Novo Usuário
        [5] - Nova conta
        [6] - Listar Usuários
        [0] - Sair

        =>:  """
    return int(input(menu))

def depositar_valor(valor, saldo, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    return saldo, extrato

def sacar_valor(valor, saldo, limite, extrato, limite_saque, numero_saque):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saque = numero_saque >= limite_saque

    if excedeu_saldo:
        print("Saque não realizado! Você não possui saldo suficiente")

    elif excedeu_limite:
        print(
            f"Saque não realizado! Valor informado ultrapassa o limite diário de: R$ {limite:.2f}")
    elif excedeu_saque:
        print("Saque não realizado! Seu limite diário de saques foi atingido")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saque += 1

    else:
        print("Saque não realizado! Valor informado para saque inválido")
    
    return saldo, extrato, numero_saque

def mostrar_extrato(saldo, extrato):
    print("\n=============EXTRATO============")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==================================")

def criar_usuario(usuarios):
    cpf = input("Digite o seu CPF, apenas números: ")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print("Usuário já cadastrado")
        return
    
    nome = input("Digite o seu nome: ")
    data_de_nascimento = input("Digite sua data de nascimento no formato DD/MM/AAAA: ")
    endereco_usuario = {
        "rua": input("Digite a Rua do endereço com numero: "),
        "bairro": input("Digite o Bairro do endereço: "),
        "cidade": input("Digite a Cidade do endereço: "),
        "estado": input("Digite o Estado do endereço: ")
    }

    novo_usuario = {
        "nome": nome,
        "data": data_de_nascimento,
        "cpf": cpf,
        "endereco": {},
        "contas": []
    }

    novo_usuario["endereco"] = endereco_usuario
    usuarios.append(novo_usuario)
    
def filtrar_usuarios(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def main():
    AGENCIA = "0001"
    saldo = 0
    limite = 500
    extrato = ""
    numero_saque = 0
    LIMITE_SAQUE = 3
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == 1:
            valor = float(input("Digite o valor que deseja despositar: "))

            saldo, extrato = depositar_valor(valor=valor, saldo=saldo, extrato=extrato)

        elif opcao == 2:
            valor = float(input("Digite o valor que deseja sacar: "))

            saldo, extrato, numero_saque = sacar_valor(valor=valor, saldo=saldo, limite=limite, extrato=extrato, limite_saque=LIMITE_SAQUE, numero_saque=numero_saque)

        elif opcao == 3:
            mostrar_extrato(saldo=saldo, extrato=extrato)

        elif opcao == 4:
            criar_usuario(usuarios)
        
        elif opcao == 5:
            print

        elif opcao == 6:
            for usuario in usuarios:
                print("Usuário:", usuario["nome"])
                print("CPF:", usuario["cpf"])
                print("Contas vinculadas:")
            for conta in usuario["contas"]:
                print("Agência:", conta["agencia"])
                print("Número da Conta:", conta["numero_conta"])
                print("--------------------")

        elif opcao == 0:
            break

        else:
            print("Opção inválida, por favor selecione alguma opção válida")

main()