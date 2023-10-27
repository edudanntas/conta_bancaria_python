def menu():
    menu = """

        [1] - Depositar
        [2] - Sacar
        [3] - Extrato
        [0] - Sair

        => """
    return int(input(menu))

def depositar_valor(valor, saldo, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    return saldo, extrato


def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saque = 0
    LIMITE_SAQUE = 3

    while True:
        opcao = menu()

        if opcao == 1:
            valor = float(input("Digite o valor que deseja despositar: "))

            saldo, extrato = depositar_valor(valor=valor, saldo=saldo, extrato=extrato)

        elif opcao == 2:
            valor_saque = float(input("Digite o valor que deseja sacar: "))

            excedeu_saldo = valor_saque > saldo
            excedeu_limite = valor_saque > limite
            excedeu_saque = numero_saque >= LIMITE_SAQUE

            if excedeu_saldo:
                print("Saque não realizado! Você não possui saldo suficiente")

            elif excedeu_limite:
                print(
                    f"Saque não realizado! Valor informado ultrapassa o limite diário de: R$ {limite:.2f}")

            elif excedeu_saque:
                print("Saque não realizado! Seu limite diário de saques foi atingido")

            elif valor_saque > 0:
                saldo -= valor_saque
                extrato += f"Saque: R$ {valor_saque:.2f}\n"
                numero_saque += 1

            else:
                print("Saque não realizado! Valor informado para saque inválido")

        elif opcao == 3:
            print("\n=============EXTRATO============")
            print("Não foram realizadas movimentações." if not extrato else extrato)
            print(f"\nSaldo: R$ {saldo:.2f}")
            print("==================================")

        elif opcao == 0:
            break

        else:
            print("Opção inválida, por favor selecione alguma opção válida")

main()