from random import randint

# Superclasse Agencia
class Agencia:
    def __init__(self, telefone, cnpj, numero):
        self.telefone = telefone
        self.cnpj = cnpj
        self.numero = numero
        # Relação de clientes da Agencia
        self.clientes = []
        # Dinheiro em caixa disponivel para emprestimos
        self.caixa = 0
        # Registro de emprestimos aos clientes
        self.emprestimos = []

    # Sempre que o caixa da agencia estiver com montante abaixo
    # do limite, um alerta será emitido.
    # No nosso exemplo, o limite será R$ 1.000.000,00
    def verificar_caixa(self):
        if self.caixa < 1000000:
            print('Caixa abaixo do nivel recomendado. Caixa Atual: {}'.format(self.caixa))
        else:
            print('O valor do Caixa está OK. Caixa Atual: {}'.format(self.caixa))

    def emprestar_dinheiro(self, valor, cpf, juros):
        if self.caixa > valor:
            self.emprestimos.append((valor, cpf, juros))
            print('Empréstimo efetuado!')
        else:
            print('Não é possível o empréstimo! Dinheiro não disponivel em caixa!')

    def adicionar_cliente(self, nome, cpf, patrimonio):
        self.clientes.append((nome, cpf, patrimonio))

# Subclasse AgenciaVirtual
class AgenciaVirtual(Agencia):
    def __init__(self, site, telefone, cnpj):
        self.site = site
        super().__init__(telefone, cnpj, 1000)
        self.caixa = 1000000
        self.caixa_paypal = 0
        self.email = ''

    # Polimorfismo de metodo
    def adicionar_cliente(self, nome, cpf, patrimonio, email):
        super().adicionar_cliente(nome, cpf, patrimonio)
        self.email = email
        self.clientes.append((nome, cpf, patrimonio, email))

    def depositar_paypal(self, valor):
        self.caixa -= valor
        self.caixa_paypal += valor

    def sacar_paypal(self, valor):
        self.caixa_paypal -= valor
        self.caixa += valor


class AgenciaComum(Agencia):
    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, numero = randint(1001, 5999))
        self.caixa = 1000000
