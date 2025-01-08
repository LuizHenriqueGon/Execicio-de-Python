km_percorridos = float(input('Digite a quantidade de km percorridos: '))
dias_alugados = int(input('Digite a quantidade de dias pelos quais o carro foi alugado: '))

preco_por_dia = 60.00
preco_por_km = 0.15

custo_dias = dias_alugados * preco_por_dia
custo_km = km_percorridos * custo_dias
preco_total = custo_km * preco_por_km

print(f"Valor a pagar pelos dias: R${custo_dias:.2f}")
print(f"Valor a pagar pelos km percorridos: R${custo_km:.2f}")
print(f"Preço total a pagar: R${preco_total:.2f}")

