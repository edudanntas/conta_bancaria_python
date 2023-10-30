
# Projeto de Conta Bancária em Python

Este é um simples projeto de conta bancária em Python que permite realizar operações bancárias como depósitos, saques e verificar o extrato.


## Funcionalidades

- Depositar dinheiro na conta.
- Sacar dinheiro da conta, com limites diários de saque.
- Verificar o extrato da conta.
- Criar um novo usuário (cliente).
- Criar uma nova conta vinculada a um usuário.
- Listar as contas cadastradas.
- Registro de transações.


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
    [4] - Novo Usuário
    [5] - Nova conta
    [6] - Listar contas
    [0] - Sair
    ```

4. Selecione a opção desejada digitando o número correspondente.

5. Siga as instruções no console para realizar depósitos, saques, criar novos usuários, criar novas contas ou listar contas cadastradas.

    
## Requisitos

- Python 3.x

## Exemplo de Uso

Logo abaixo está um exemplo de uso do projeto:

1. Depositar dinheiro na conta:
    ```bash
    [1] - Depositar
    (Digite o seu CPF e o valor que deseja depositar)
    ```
2. Sacar dinheiro da conta:
    ```bash
    [2] - Sacar
    (Digite o seu CPF e o valor que deseja sacar)
    ```
    Você pode receber mensagens de erro se tentar sacar mais do que o saldo disponível, exceder o limite diário de saque ou atingir o limite diário de saques.

3. Verificar o extrato da conta:
    ```bash
    [3] - Extrato
    (Digite o seu CPF)
    ```
    O extrato mostrará as transações registradas na conta.

4. Criar um novo usuário (cliente):
    ```bash
    [4] - Novo Usuário
    (Siga as instruções para fornecer informações do novo cliente)
    ```

5. Criar uma nova conta vinculada a um usuário:
    ```bash
    [5] - Nova conta
    (Digite o seu CPF para vincular a conta)
    ```

6. Listar as contas cadastradas:
    ```bash
    [6] - Listar contas
    (Listagem das contas cadastradas será exibida)
    ```

7. Sair do programa:
    ```bash
    [0] - Sair
    ```

## Entendendo as Classes

### `Cliente`

A classe `Cliente` representa um cliente do banco. Cada cliente possui um endereço e pode ter várias contas bancárias. 

**Atributos:**
- `endereco`: O endereço do cliente.
- `contas`: Uma lista das contas associadas a este cliente.

A classe fornece métodos para realizar transações e adicionar contas.

### `PessoaFisica`

A classe `PessoaFisica` é uma subclasse de `Cliente` e representa um cliente do banco que é uma pessoa física. Ela armazena informações adicionais, como nome, data de nascimento e CPF.

**Atributos:**
- `nome`: O nome do cliente.
- `data_nascimento`: A data de nascimento do cliente.
- `cpf`: O CPF do cliente.

### `Conta`

A classe `Conta` representa uma conta bancária. Cada conta possui um número, um saldo, uma agência e um cliente associado. Além disso, a classe mantém um histórico de transações.

**Atributos:**
- `numero`: O número da conta.
- `saldo`: O saldo da conta.
- `agencia`: A agência da conta.
- `cliente`: O cliente associado à conta.
- `historico`: O histórico de transações da conta.

### `ContaCorrente`

A classe `ContaCorrente` é uma subclasse de `Conta` e representa uma conta corrente. Ela adiciona funcionalidades específicas, como limites de saque e número máximo de saques.

**Atributos:**
- `limite`: O limite de saque da conta corrente.
- `limite_saques`: O número máximo de saques permitidos.

### `Historico`

A classe `Historico` mantém um registro das transações realizadas em uma conta. Ela armazena informações como o tipo de transação, o valor e a data da transação.

**Atributos:**
- `transacoes`: Uma lista de transações registradas.

### `Transacao` (Classe Abstrata)

A classe `Transacao` é uma classe abstrata que define a estrutura básica de uma transação. Ela possui métodos abstratos para obter o valor da transação e registrar a transação em uma conta.

**Métodos Abstratos:**
- `valor`: Método abstrato para obter o valor da transação.
- `registrar`: Método abstrato para registrar a transação em uma conta.

### `Sacar` e `Deposito` (Subclasses de `Transacao`)

As classes `Sacar` e `Deposito` são subclasses de `Transacao` que implementam os métodos abstratos. Elas representam transações de saque e depósito, respectivamente, e são usadas para registrar essas transações em uma conta.

**Atributos:**
- `valor`: O valor da transação.

## Contribuindo

Se você deseja contribuir para este projeto, sinta-se à vontade para abrir problemas (issues) e enviar solicitações de pull (pull requests).


## Licença

Este projeto está licenciado sob a Licença MIT - consulte o arquivo LICENSE para obter detalhes.

