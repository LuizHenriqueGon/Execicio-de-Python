# Programa Principal
# Importações das classes e módulos necessários
from Contas import ContaCorrente  # Classe para gerenciar contas correntes
from Contas import CartaoCredito  # Classe para gerenciar cartões de crédito
from Agencia import Agencia, AgenciaVirtual  # Classes para agências físicas e virtuais

# Criação de uma conta corrente para o cliente "Juca"
conta_juca = ContaCorrente("Juca", "123.456.789-10", "0115", "5454")
print('Cliente: ', conta_juca.nome)
print('CPF: ', conta_juca.cpf)
print('Saldo inicial: R$', conta_juca.saldo)

# Operação de depósito
print("\n>>> Depositando R$ 10.000,00 na conta de Juca.")
conta_juca.depositar_dinheiro(10000)
conta_juca.consultar_historico_transacoes()

# Operação de saque
print("\n>>> Sacando R$ 1.000,00 da conta de Juca.")
conta_juca.sacar_dinheiro(1000)
conta_juca.consultar_historico_transacoes()

# Transferência entre contas
print("\n>>> Criando conta para a mãe de Juca e realizando transferência de R$ 1.000,00.")
conta_maeJuca = ContaCorrente('Sara', '111.444.777-35', '4433', '5454')
conta_juca.transferir(1000, conta_maeJuca)
print("Saldo da conta de Sara:")
conta_maeJuca.consultar_saldo()

print("Histórico de transações de Juca:")
conta_juca.consultar_historico_transacoes()

print("Histórico de transações de Sara:")
conta_maeJuca.consultar_historico_transacoes()

# Criando um cartão de crédito associado à conta de Juca
print("\n>>> Criando cartão de crédito para Juca.")
cartao_juca = CartaoCredito("Juca", conta_juca)
print("Informações do cartão de crédito de Juca:", cartao_juca.__dict__)
print("\nAlterando a senha do cartão:")
cartao_juca.senha = '1234'  # Senha definida
print("Nova senha definida:", cartao_juca.senha)

# Trabalhando com Agências
print("\n>>> Criando uma agência física.")
agencia1 = Agencia('2222-3333', '123.456.789/0001-10', 4568)
agencia1.caixa = 2000000
print("Dados da Agência 1:", agencia1.__dict__)

print("\n>>> Realizando empréstimo de R$ 10.000,00.")
agencia1.emprestar_dinheiro(10000, '123.456.789-10', 0.1)

print("Adicionando Juca como cliente da agência.")
agencia1.adicionar_clientes('Juca', '123.456.789-10', 100000)
print("Clientes da agência:", agencia1.clientes)

# Criando uma agência virtual
print("\n>>> Criando uma agência virtual.")
agencia_virtual = AgenciaVirtual('www.agenciavirtual.com.br', '3333-5555', '34.456.678/001-87')
agencia_virtual.depositar_paypal(1000)  # Operação de depósito no PayPal
print("Dados da Agência Virtual:", agencia_virtual.__dict__)

# Polimorfismo de objeto: atribuindo uma agência virtual a uma variável genérica de agência
agencia2 = agencia_virtual
print("\n>>> Trabalhando com polimorfismo.")
print("Site da Agência 2 (polimorfismo):", agencia2.site)

# Adicionando input ao programa principal
print("\n>>> INTERAÇÃO DO USUÁRIO")
nome_cliente = input("Digite o nome do cliente para criar uma nova conta: ")
cpf_cliente = input("Digite o CPF do cliente: ")
agencia_cliente = input("Digite o número da agência: ")
conta_cliente = input("Digite o número da conta: ")

nova_conta = ContaCorrente(nome_cliente, cpf_cliente, agencia_cliente, conta_cliente)
print("\nNova conta criada com sucesso!")
print(f"Cliente: {nova_conta.nome}, CPF: {nova_conta.cpf}, Agência: {nova_conta.agencia}, Conta: {nova_conta.numero}")
