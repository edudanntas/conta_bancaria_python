from abc import ABC, abstractmethod, abstractproperty
from datetime import datetime

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

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite_saque=3, limite=500):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saque = limite_saque

    def sacar(self, valor):
        numero_saques = len([transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__])

        excedeu_limite = valor > self.limite_saque
        excedeu_saque = numero_saques >= self.limite_saque

        if excedeu_limite: 
            print("Valor de saque indisponivel, limite atingido")
        
        elif excedeu_saque:
            print("Transações diárias de saque excedidas, por favor, tente novamente outro dia")

        else:
            return super().sacar(valor)

        return False

    def __str__(self):
        return f"""
        Agencia:\t{self.agencia}
        C/C:\t\t{self.numero}
        Titular:\t{self.cliente.nome}
        """

class Historico:
    def __init__(self):
        self._transacoes = []
    
    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%s")
            }
        )

class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass

class Sacar(Transacao):
    
    def __init__(self, valor):
        self._valor = valor
    
    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class Desposito(Transacao):
    
    def __init__(self, valor):
        self._valor = valor
    
    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


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

def depositar(clientes):
    cpf = input("Digite o seu CPF, apenas números: ")
    cliente = filtrar_cliente(cpf, cliente)

    if not cliente:
        print("Cliente não encontrado")
        return
    
    valor = float(input("Digite aqui o valor que deseja depositar: "))
    transacao = Desposito(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    cliente.realizar_transacao(conta, transacao)

def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("Cliente não possui conta :(")
        return
    return cliente.contas[0]

def sacar(clientes):
    cpf = input("Digite o seu CPF, apenas números: ")
    cliente = filtrar_cliente(cpf, cliente)

    if not cliente:
        print("Cliente não encontrado!")
        return
    
    valor = float(input("Digite o valor que deseja sacar: "))
    transacao = Sacar(valor)

    conta = recuperar_conta_cliente(cliente)

    if not conta:
        return
    
    conta.realizar_transacao(conta, transacao)

def mostrar_extrato(clientes):
    cpf = input("Digite o seu CPF, apenas números: ")
    cliente = filtrar_cliente(cpf, cliente)

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

def criar_conta(numero_conta, clientes, contas):
    cpf = input("Digite o seu CPF, apenas números: ")
    cliente = filtrar_cliente(cpf, cliente)

    if not cliente:
        print("Cliente não encontrado!")
        return
    
    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)

    print("Conta criada com sucesso")

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
            pass
        
        elif opcao == 5:
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)

        elif opcao == 6:
           pass

        elif opcao == 0:
            break

        else:
            print("Opção inválida, por favor selecione alguma opção válida")

main()