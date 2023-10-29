
class Cliente:

    def __init__(self, endereco):
        self._endereco = endereco
        self._contas = []

    def adicionar_conta(self, conta):
        self._contas.append(conta)
    
    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

class PessoaFisica(Cliente):

    def __init__(self, nome, cpf, data_nascimento):
        super().__init__(endereco)
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento


class Conta: 

    def __init__(self, saldo, numero, agencia, cliente, historico):
        self._saldo = saldo
        self._numero = numero
        self._agencia = agencia
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico

    def sacar(self, saldo, valor):
        saldo = self._saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("Transação não completada, valor maior que saldo disponivel")

        elif valor > 0:
            self._saldo -= valor
            print("\n Transação efetuada com sucesso")
            return True
        else:
            print("operação falhou")
            
        return False
    
    def depositar(self, saldo, valor):
        if valor > 0:
            self._saldo += valor
            print("Operação de despósito foi feita com sucesso")
            
        else:
            print("O valor informado é invalido, tente novamente ")
            return False
        
        return True




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
        "endereco": {}
    }

    novo_usuario["endereco"] = endereco_usuario
    usuarios.append(novo_usuario)
    
def filtrar_usuarios(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Digite o seu CPF, apenas números: ")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print("conta criada com sucesso")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("Ops, usuário não encontrado")

def listar_contas(contas):
    for conta in contas:
        lista = f"""
        Agencia:\t{conta["agencia"]}
        C/C:\t\t{conta["numero_conta"]}
        Titular:\t{conta["usuario"]["nome"]}
        """
        print("="*40)
        print(lista)

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
            numero_conta = len(contas) + 1
            conta = criar_conta(agencia=AGENCIA, numero_conta=numero_conta, usuarios=usuarios)

            if conta:
                contas.append(conta)

        elif opcao == 6:
            listar_contas(contas)

        elif opcao == 0:
            break

        else:
            print("Opção inválida, por favor selecione alguma opção válida")

main()