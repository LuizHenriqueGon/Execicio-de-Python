valor_divida = float(input("Digite o valor inicial da dívida: R$ "))
juros_mensal = float(input("Digite o juro mensal (em %): "))
pagamento_mensal = float(input("Digite o valor que será pago mensalmente: R$ "))

juros_decimal = juros_mensal / 100

meses = 0
total_pago = 0
total_juros_pago = 0

while valor_divida > 0:
    juros = valor_divida * juros_decimal
    total_juros_pago += juros
    valor_divida += juros

    valor_divida -= pagamento_mensal
    total_pago += pagamento_mensal

    if valor_divida < 0:
        valor_divida = 0

    meses += 1


print(f"Número de meses para pagar a dívida: {meses}")
print(f"Total pago: R$ {total_pago:.2f}")
print(f"Total de juros pagos: R$ {total_juros_pago:.2f}")