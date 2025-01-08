'''
Criar um sistema orientado a objetos para um caixa eletrônico.
O programa deverá perguntar ao cliente o valor do saque em sua
conta bancária e depois informar quantas notas de cada valor
serão fornecidas.
As notas disponíveis serã de 100, 50, 20, 10 e 5 reais.
O programa não deve se preocupar com a quantidade de notas existentes
na máquina.
Sabe-se que o caixa eletrônico possui um saldo de R$ 240.000,00 reais.
Quando o saldo do caixa chegar a 10% do valor montante, o sistema
deverá emitir um alerta de que o caixa está com o saldo baixo.
Um caixa eletrônico aceita saque até R$ 600,00.
Exemplo: Para sacar 245,00
O programa fornecerá duas notas de R$100,00, duas notas de R$20,00
e uma nota de R$5,00
'''

class CaixaEletronico:
    def __init__(self):
        self._saldo = 240000
        # limite minimo = 10% do saldo
        self._limite_minimo = self._saldo * 0.10
        #Lista de notas com valores decrescentes
        self.notas_disponiveis = [100, 50, 20, 10, 5]

    def verificar_saldo_baixo(self):
        if self._saldo <= self._limite_minimo:
            print('[ALETA] O saldo do caixa está baixo')

    def sacar(self, valor):
        if valor < 10 or valor > 600:
            print("[ERRO] Valor fora do limite permitido (10 a 600 reais)")
            return

        if valor > self._saldo:
            print('[ERRO] Saldo insuficiente no Caixa!')
            return

        # notas_a_fornece é um dicionario onde será armazanado
        # o valor e o número de cada nota a ser fornecida ao cliente,
        # onde, o valor de nota é a chave e a quantidade de notas o valor
        notas_a_fornecer = {}
        # o valor_restante receve o valor a ser sacado. A variável valor
        # não pode ser perdido, então, criar-se o valor restante que será
        #sebtraido do valor a sacar:
        valor_restante = valor

        for nota in self.notas_disponiveis:
            quantidade_notas = valor_restante // nota
            if quantidade_notas > 0:
                notas_a_fornecer[nota] = int(quantidade_notas)
                valor_restante = valor_restante - quantidade_notas * nota

        if valor_restante > 0:
             print("[ERRO] Não é possível realizar o saque com as notas disponiveis!")

        #Atualização do caixa
        self._saldo -= valor

        # Exibir as notas fornecidas
        print(f"Saque de R${valor} realizado com sucesso!")
        print("Notas Fornecidas: ")

        for nota, quantidade in notas_a_fornecer.items():
            print(f"-{quantidade} nota(s) de R${nota}")

