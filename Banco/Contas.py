from datetime import datetime
import pytz
from random import randint
class ContaCorrente:
    """
    Cria um objeto ContaCorrente para gerenciar as contas dos clientes
    nome (str): nome do cliente
    CPF (str): CPF do cliente, deve ser inserido com pontos e traços (xxx.xxx.xxx-xx)
    agencia (str): número da agência
    num_conta (str): número da conta corrente do cliente
    saldo (float): saldo disponível pelo cliente
    limite (float): limite do cheque especial do cliente
    transações (list): histórico de transações do cliente
    """
    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR.strftime('%d/%m/%Y %H:%M:%S')

    # Contrutor da classe
    def __init__(self, nome, cpf, agencia, num_conta):
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0
        self.limite = None
        self.agencia = agencia
        self.num_conta = num_conta
        self.transacoes = []
        self.cartoes = []

    # Método para consulta do saldo da conta corrente
    def consultar_saldo(self):
        print('Seu Saldo atual é de R$ {:,.2f}'.format(self.saldo))
        pass

    def depositar_dinheiro(self, valor):
        self.saldo += valor
        self.transacoes.append((valor, self.saldo, ContaCorrente._data_hora()))
        pass

    def sacar_dinheiro(self, valor):
        if self.saldo - valor < self._limite_conta():
            print("Você não possui saldo suficiente para sacar este valor!")
        else:
            self.saldo -= valor
            self.transacoes.append((valor, self.saldo, ContaCorrente._data_hora()))
        pass

    def _limite_conta(self):
        self.limite = -1000
        return self.limite

    def consultar_historico_transacoes(self):
        print('Histórico de Transações:')
        for transacao in self.transacoes:
            print(transacao)

    def transferir(self, valor, conta_destino):
        # Conta de Origem
        self.saldo -= valor
        self.transacoes.append((-valor, self.saldo, ContaCorrente._data_hora()))
        # Conta de Destino
        conta_destino.saldo += valor
        conta_destino.transacoes.append((valor, conta_destino.saldo, ContaCorrente._data_hora()))

class CartaoCredito:
    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR

    def __init__(self, titular, conta_corrente):
        self.titular = titular
        self.conta_corrente = conta_corrente
        self.numero = randint(1000000000000000, 9999999999999999)
        # A validade está com problemas, provavelmente, em virtude da atualização da biblioteca pytz
        self.validade = '{}/{}'.format(CartaoCredito._data_hora().month, CartaoCredito._data_hora().year + 4)
        self.cod_seguranca = '{}{}{}'.format(randint(0, 9), randint(0, 9), randint(0, 9))
        self.limite = 1000
        self.__senha = '1234'
        conta_corrente.cartoes.append(self)

    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, valor):
        if len(valor) == 4 and valor.isnumeric():
            self.__senha = valor
        else:
            print("Nova senha inválida!")


