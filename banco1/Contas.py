from datetime import datetime
import pytz
from random import randint

class ContaCorrente:
    """
    Classe que representa uma conta corrente para gerenciar as contas dos clientes.
    Atributos:
        - nome (str): Nome do cliente.
        - cpf (str): CPF do cliente, no formato xxx.xxx.xxx-xx.
        - agencia (str): Número da agência.
        - num_conta (str): Número da conta corrente do cliente.
        - saldo (float): Saldo disponível.
        - limite (float): Limite de cheque especial.
        - transacoes (list): Histórico de transações do cliente.
    """

    @staticmethod
    def _data_hora():
        """
        Retorna a data e hora atual no fuso horário brasileiro.
        """
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR.strftime('%d/%m/%Y %H:%M:%S')

    def __init__(self, nome, cpf, agencia, num_conta):
        """
        Construtor da classe ContaCorrente.
        Inicializa os atributos básicos de uma conta corrente.
        """
        self.nome = nome  # Nome do titular da conta
        self.cpf = cpf  # CPF do titular
        self.saldo = 0  # Saldo inicial
        self.limite = None  # Limite de cheque especial (definido no método privado)
        self.agencia = agencia  # Número da agência
        self.num_conta = num_conta  # Número da conta
        self.transacoes = []  # Lista para armazenar o histórico de transações
        self.cartoes = []  # Lista de cartões de crédito associados

    def consultar_saldo(self):
        """
        Exibe o saldo atual da conta corrente.
        """
        print('Seu Saldo atual é de R$ {:,.2f}'.format(self.saldo))

    def depositar_dinheiro(self, valor):
        """
        Adiciona um valor ao saldo da conta corrente e registra a transação.
        :param valor: Valor a ser depositado.
        """
        self.saldo += valor
        self.transacoes.append((valor, self.saldo, ContaCorrente._data_hora()))

    def sacar_dinheiro(self, valor):
        """
        Deduz um valor do saldo, respeitando o limite da conta.
        :param valor: Valor a ser sacado.
        """
        if self.saldo - valor < self._limite_conta():
            print("Você não possui saldo suficiente para sacar este valor!")
        else:
            self.saldo -= valor
            self.transacoes.append((-valor, self.saldo, ContaCorrente._data_hora()))

    def _limite_conta(self):
        """
        Define o limite de cheque especial da conta.
        :return: Limite da conta.
        """
        self.limite = -1000
        return self.limite

    def consultar_historico_transacoes(self):
        """
        Exibe o histórico de transações da conta corrente.
        """
        print('Histórico de Transações:')
        for transacao in self.transacoes:
            print(transacao)

    def transferir(self, valor, conta_destino):
        """
        Realiza uma transferência entre contas correntes.
        :param valor: Valor a ser transferido.
        :param conta_destino: Objeto da conta que receberá o valor.
        """
        # Deduz o valor da conta de origem
        self.saldo -= valor
        self.transacoes.append((-valor, self.saldo, ContaCorrente._data_hora()))

        # Adiciona o valor à conta de destino
        conta_destino.saldo += valor
        conta_destino.transacoes.append((valor, conta_destino.saldo, ContaCorrente._data_hora()))


class CartaoCredito:
    """
    Classe que representa um cartão de crédito vinculado a uma conta corrente.
    """

    @staticmethod
    def _data_hora():
        """
        Retorna a data e hora atual no fuso horário brasileiro.
        """
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR

    def __init__(self, titular, conta_corrente):
        """
        Construtor da classe CartaoCredito.
        :param titular: Nome do titular do cartão.
        :param conta_corrente: Objeto da conta corrente associada.
        """
        self.titular = titular  # Nome do titular
        self.conta_corrente = conta_corrente  # Conta associada
        self.numero = randint(1000000000000000, 9999999999999999)  # Número do cartão gerado aleatoriamente
        self.validade = '{}/{}'.format(CartaoCredito._data_hora().month, CartaoCredito._data_hora().year + 4)  # Validade do cartão
        self.cod_seguranca = '{}{}{}'.format(randint(0, 9), randint(0, 9), randint(0, 9))  # Código de segurança (CVV)
        self.limite = 1000  # Limite inicial do cartão
        self.__senha = '1234'  # Senha padrão
        conta_corrente.cartoes.append(self)  # Associa o cartão à conta corrente

    @property
    def senha(self):
        """
        Retorna a senha do cartão (protegida por encapsulamento).
        """
        return self.__senha

    @senha.setter
    def senha(self, valor):
        """
        Define uma nova senha para o cartão.
        :param valor: Nova senha (deve ser numérica e ter 4 dígitos).
        """
        if len(valor) == 4 and valor.isnumeric():
            self.__senha = valor
        else:
            print("Nova senha inválida!")

