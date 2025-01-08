dias = int(input("Digite a quantidade de dias: "))
horas = int(input("Digite a quantidade de horas: "))
minutos = int(input("Digite a quantidade de minutos: "))
sengundos = int(input("Digite a quantidade de sengundos: "))

total_seguntos = dias * 86400 + horas * 3600 + minutos * 60 + sengundos

print(f"O total em segundo é: {total_seguntos} sengundos")