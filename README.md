
# Projeto de Conta Bancária em Python

Este é um simples projeto de conta bancária em Python que permite realizar operações bancárias como depósitos, saques e verificar o extrato.


## Funcionalidades

- Depositar dinheiro na conta.
- Sacar dinheiro da conta, com limites diários de saque.
- Verificar o extrato da conta.
- Sair do programa.


## Instruções de Uso

1. Clone o repositório para a sua máquina local:

   ```bash
   git clone https://github.com/edudanntas/conta_bancaria_python.git
   ```

2. Execute o arquivo conta_bancaria.py:

    ```bash
    python conta_bancaria.py
    ```

3. Você verá o seguinte menu:
    ```bash
    [1] - Depositar
    [2] - Sacar
    [3] - Extrato
    [0] - Sair
    ```

4. Selecione a opção desejada digitando o número correspondente.

5. Siga as instruções no console para realizar depósitos, saques ou verificar o extrato.

    
## Requisitos

- Python 3.x

## Exemplo de Uso

Logo abaixo está um exemplo de uso do projeto:

1. Depositar dinheiro na conta:
    ```bash
    [1] - Depositar
    Digite o valor que deseja depositar: 100.00
    ```
2. Sacar dinheiro da conta:
    ```bash
    [2] - Sacar
    Digite o valor que deseja sacar: 50.00

    ```
    Você pode receber mensagens de erro se tentar sacar mais do que o saldo disponível, exceder o limite diário de saque ou atingir o limite diário de saques.

3. Verificar o extrato da conta:
    ```bash
    [3] - Extrato

    =============EXTRATO============
    Depósito: R$ 100.00
    Saque: R$ 50.00

    Saldo: R$ 50.00
    ==================================
    ```

4. Sair do programa:
    ```bash
    [0] - Sair
    ```
## Contribuindo

Se você deseja contribuir para este projeto, sinta-se à vontade para abrir problemas (issues) e enviar solicitações de pull (pull requests).


## Licença

Este projeto está licenciado sob a Licença MIT - consulte o arquivo LICENSE para obter detalhes.

