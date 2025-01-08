# Programa Principal
from Contas import ContaCorrente
from Contas import CartaoCredito
from Agencia import Agencia, AgenciaVirtual

conta_juca = ContaCorrente("Juca", "123.456.789-10", "0115", "5454")
print('Cliente: ', conta_juca.nome)
print('CPF: ', conta_juca.cpf)
print('Saldo = ', conta_juca.saldo)

# Depositando R$ 10.000,00
conta_juca.depositar_dinheiro(10000)
conta_juca.consultar_historico_transacoes()
# Saque de R$ 1.000,00
conta_juca.sacar_dinheiro(1000)
conta_juca.consultar_historico_transacoes()
# Criando a conta da mãe do juca
conta_maeJuca = ContaCorrente('Sara', '111.444.777-35', '4433', '5454')
conta_juca.transferir(1000, conta_maeJuca)
conta_maeJuca.consultar_saldo()
conta_juca.consultar_historico_transacoes()
conta_maeJuca.consultar_historico_transacoes()
cartao_juca = CartaoCredito("Juca", conta_juca)
# help(ContaCorrente)
#print(cartao_juca.titular)
#print(cartao_juca.numero)
#print(cartao_juca.validade)
#print(cartao_juca.cod_seguranca)
print(cartao_juca.__dict__)
cartao_juca.senha= '12'
cartao_juca.senha= 'asdg'
cartao_juca.senha= '2345'
print(cartao_juca.senha)
#Agencia
agencia1 = Agencia('2222-3333','123.456.789/0001-10', 4568)
agencia1.caixa = 2000000
print('Dados da Agencia 1:')
print(agencia1.__dict__)
print(agencia1.verificar_caixa())
agencia1.emprestar_dinheiro(10000 ,'123.456.789-10', 0.1)
agencia1.adicionar_clientes('Juca', '123.456.789-10', 100000)
print(agencia1.clientes)
print(agencia1.__dict__)
#Agencia virtual
print('Agencia Virtual')
agencia_virtual = AgenciaVirtual('www.agenciavirtual.com.br', '3333-5555','34.456.678/001-87')
agencia_virtual.verificar_caixa()
print(agencia_virtual.__dict__)
agencia_virtual.depositar_paypal(1000)
print('Agencia Virtual: ', agencia_virtual.caixa)
print('Caixa Paypal Agencia Virtual: ', agencia_virtual.caixa_paypal)
agencia_virtual.adicionar_clientes('Joca', '163.457.789-11', 10000, 'joca@gmail.com')
print('asd')
print(agencia_virtual.__dict__)

print('Agencia 2')

#Polimorfismo de objeto
agencia2 = Agencia('4343','222.333.244/0001-49', '8978')
agencia2 = agencia_virtual
print("Site Agencia 2: ",agencia2.site)