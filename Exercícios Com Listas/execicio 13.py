#Faça um programa que receba a temperatura média de cada mês do ano e
# armazene-as em uma lista. Após isto, calcule a média anual das
# temperaturas e mostre todas as temperaturas acima da média anual,
# e em que mês elas ocorreram
# (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).
from statistics import median

temperaturas = []

meses = ["Janeiro", "Fevereiro","Março","Abril", "Maio", "Julho",
         "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

for i in range(12):
    temperatura = float(input(f"Digite a temperatura média de {meses[i]}: "))
    temperaturas.append(temperatura)

media_anual = sum(temperaturas)/len(temperaturas)
print(f"Média anual de temperatura: {media_anual:.2f}°C")
print(f"Meses com temperaturas acima da média anual: ")

for i in range(12):
    if temperaturas[i] > media_anual:
        print(f"{meses[i]}: {temperaturas[i]:.2f}°C")
