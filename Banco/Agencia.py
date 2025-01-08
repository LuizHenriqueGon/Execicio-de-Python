from random import randint

# superclasse agencia
class Agencia:
    def __init__(self, telefone, cnpj, numero):
        self.telefone = telefone
        self.cnpj = cnpj
        self.numero = numero
        #relação de clientes da agencia
        self.clientes = []
        #Dinherio em caixa disponivel para emprestimos
        self.caixa = 0
        #Registro de emprestimos aos clientes
        self.emprestimos = []

    # Sempre que a caixa da agencia estiver com montante abaixo do limite, um
    #alerta séra emitido.
    #No nosso exemplo, o limite sera R$ 1.000.000,00
    def verificar_caixa(self):
        if self.caixa < 1000000:
            print('Caixa abaixo do nivel recomendado. Caixa Atual {}'.format(self.caixa))
        else:
            print('O valor do Caixa está OK. Caixa Atual {}'.format(self.caixa))

    def emprestar_dinheiro(self, valor, cpf, juros):
        if self.caixa > valor:
            self.emprestimos.append((valor, cpf, juros))
            print('Emprestimo realizado com sucesso!')
        else:
            print('Não é possível o emprestimo! Dinheiro não disponivel em caixa!')

    def adicionar_clientes(self, nome, cpf, patrimonio):
        self.clientes.append((nome, cpf, patrimonio))

# subclasse Agencia
class AgenciaVirtual(Agencia):
    def __init__(self, site, telefone, cnpj):
        self.site = site
        super().__init__(telefone, cnpj, numero=1000)
        self.caixa = 1000000
        self.caixa_paypal = 0
        self.email = ''

    # Polimorfismo de metodo
    def adicionar_clientes(self, nome, cpf, patrimonio, email):
        self.email = email
        self.clientes.append((nome, cpf, patrimonio, email))
        super().adicionar_clientes(nome, cpf, patrimonio)

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