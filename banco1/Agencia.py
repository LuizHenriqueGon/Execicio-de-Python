from random import randint

# Superclasse Agencia
class Agencia:
    """
    Classe que representa uma agência bancária.
    """
    def __init__(self, telefone, cnpj, numero):
        # Inicializa os atributos básicos da agência
        self.telefone = telefone  # Telefone da agência
        self.cnpj = cnpj  # CNPJ da agência
        self.numero = numero  # Número identificador da agência

        # Lista para armazenar os clientes da agência
        self.clientes = []

        # Quantia disponível em caixa para operações financeiras (como empréstimos)
        self.caixa = 0

        # Lista para registrar os empréstimos realizados
        self.emprestimos = []

    def verificar_caixa(self):
        """
        Verifica se o valor do caixa está acima do limite recomendado (R$ 1.000.000,00).
        """
        if self.caixa < 1000000:
            print(f"Caixa abaixo do nível recomendado. Caixa atual: R$ {self.caixa}")
        else:
            print(f"O valor do caixa está OK. Caixa atual: R$ {self.caixa}")

    def emprestar_dinheiro(self, valor, cpf, juros):
        """
        Realiza um empréstimo para um cliente caso o valor esteja disponível no caixa.
        :param valor: Valor a ser emprestado.
        :param cpf: CPF do cliente que receberá o empréstimo.
        :param juros: Taxa de juros aplicada ao empréstimo.
        """
        if self.caixa > valor:
            self.emprestimos.append((valor, cpf, juros))
            print("Empréstimo realizado com sucesso!")
        else:
            print("Não é possível realizar o empréstimo! Dinheiro insuficiente no caixa.")

    def adicionar_clientes(self, nome, cpf, patrimonio):
        """
        Adiciona um cliente à lista de clientes da agência.
        :param nome: Nome do cliente.
        :param cpf: CPF do cliente.
        :param patrimonio: Patrimônio do cliente.
        """
        self.clientes.append((nome, cpf, patrimonio))

# Subclasse AgenciaVirtual
class AgenciaVirtual(Agencia):
    """
    Classe que representa uma agência virtual, herda da classe Agência.
    """
    def __init__(self, site, telefone, cnpj):
        # Atributo específico da Agência Virtual
        self.site = site  # URL do site da agência

        # Chama o construtor da superclasse com número fixo para agência virtual
        super().__init__(telefone, cnpj, numero=1000)

        # Configuração inicial do caixa e do caixa PayPal
        self.caixa = 1000000  # Valor inicial do caixa
        self.caixa_paypal = 0  # Valor inicial do caixa do PayPal
        self.email = ''  # E-mail do cliente (será preenchido ao adicionar clientes)

    def adicionar_clientes(self, nome, cpf, patrimonio, email):
        """
        Adiciona um cliente à agência virtual. Inclui o e-mail como atributo adicional.
        :param nome: Nome do cliente.
        :param cpf: CPF do cliente.
        :param patrimonio: Patrimônio do cliente.
        :param email: E-mail do cliente.
        """
        self.email = email
        # Adiciona o cliente à lista com o e-mail específico
        self.clientes.append((nome, cpf, patrimonio, email))
        # Adiciona o cliente na superclasse (sem o e-mail)
        super().adicionar_clientes(nome, cpf, patrimonio)

    def depositar_paypal(self, valor):
        """
        Transfere um valor do caixa geral para o caixa PayPal.
        :param valor: Quantia a ser transferida.
        """
        self.caixa -= valor
        self.caixa_paypal += valor

    def sacar_paypal(self, valor):
        """
        Transfere um valor do caixa PayPal para o caixa geral.
        :param valor: Quantia a ser transferida.
        """
        self.caixa_paypal -= valor
        self.caixa += valor

# Subclasse AgenciaComum
class AgenciaComum(Agencia):
    """
    Classe que representa uma agência comum, herda da classe Agência.
    """
    def __init__(self, telefone, cnpj):
        # Chama o construtor da superclasse com número aleatório para a agência comum
        super().__init__(telefone, cnpj, numero=randint(1001, 5999))

        # Configuração inicial do caixa
        self.caixa = 1000000  # Valor inicial do caixa
