cigarros_por_dia = int(input("Digite a quantidade de cigaros fumados por dia:"))
anos_fumando = int(input("Digite a quantidade de anos que você já fumou: "))

cigarros_totais = cigarros_por_dia * anos_fumando * 365
minutos_perdidos = cigarros_totais * 10
dis_perdidos = minutos_perdidos / 1440

print(f"Você perdeu aproximadante {dis_perdidos:.2f} dias de vida devido ao fumo.")

