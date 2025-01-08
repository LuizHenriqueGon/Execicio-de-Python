from Caixa import CaixaEletronico
caixa = CaixaEletronico()
valor = float(input('Entre com um valor a sacar: R$ '))
caixa.sacar(valor)