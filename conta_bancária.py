from classes import Cliente, PessoaFisica, Conta, ContaCorrente, Historico, Transacao, Deposito, Sacar

def menu():
    menu = """

        [1] - Depositar
        [2] - Sacar
        [3] - Extrato
        [4] - Novo Usuário
        [5] - Nova conta
        [6] - Listar contas
        [0] - Sair

        =>:  """
    return int(input(menu))

def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("Cliente não possui conta :(")
        return
    return cliente.contas[0]

def depositar(clientes):
    cpf = input("Digite o seu CPF, apenas números: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("Cliente não encontrado")
        return
    
    valor = float(input("Digite aqui o valor que deseja depositar: "))
    transacao = Deposito(valor)

    conta = recuperar_conta_cliente(cliente)

    if not conta:
        print()
        return
    
    cliente.realizar_transacao(conta, transacao)

def sacar(clientes):
    cpf = input("Digite o seu CPF, apenas números: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("Cliente não encontrado")
        return
    
    valor = float(input("Digite aqui o valor que deseja sacar: "))
    transacao = Sacar(valor)

    conta = recuperar_conta_cliente(cliente)

    if not conta:
        print()
        return
    
    cliente.realizar_transacao(conta, transacao)

def mostrar_extrato(clientes):
    cpf = input("Digite o seu CPF, apenas números: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("Cliente não encontrado!")
        return
    
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    print("\n================= EXTRATO =================")

    transacoes = conta.historico.transacoes

    extrato = ""

    if not transacoes:
        print("Não foram feitas movimentações")
    else: 
        for transacao in transacoes:
            extrato += f"\n{transacao['tipo']}: \n\tR$ {transacao['valor']:.2f}"
            
    print(extrato)
    print(f"\nSaldo: \n\tR$ {conta.saldo:.2f}")
    print("=" *45)

def criar_cliente(clientes):
    cpf = input("Digite o seu CPF, apenas números: ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print("Cliente Já existe em nossos sistemas")
        return
    
    nome = input("Digite o seu nome: ")
    data_nascimento = input("Digite sua data de nascimento no formato DD-MM-AAAA: ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla do estado: ")

    cliente = PessoaFisica(nome=nome, cpf=cpf, data_nascimento=data_nascimento, endereco=endereco)

    clientes.append(cliente)

    print("Cliente Adicionado com sucesso")

def criar_conta(numero_conta, clientes, contas):
    cpf = input("Digite o seu CPF, apenas números: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("Cliente não encontrado!")
        return
    
    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)

    print("Conta criada com sucesso")

def listar_contas(contas):
    for conta in contas:
        print("=" *100)
        print(conta)

def main():
    clientes = []
    contas = []

    while True:
        opcao = menu()

        if opcao == 1:
            depositar(clientes)

        elif opcao == 2:
            sacar(clientes)

        elif opcao == 3:
            mostrar_extrato(clientes)

        elif opcao == 4:
            criar_cliente(clientes)
        
        elif opcao == 5:
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)

        elif opcao == 6:
           listar_contas(contas)

        elif opcao == 0:
            break

        else:
            print("Opção inválida, por favor selecione alguma opção válida")

main()