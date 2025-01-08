#Faça um Programa que leia dois listas com 10 elementos cada.
# Gere um terceiro lista de 20 elementos,
# cujos valores deverão ser compostos pelos elementos intercalados dos dois outras listas.
lista1 = []
lista2 = []

print("Digite 10 números para a primeira lista: ")
for i in range(5):
    numero = int(input(f"Números {i+1}: "))
    lista1.append(numero)

print("Digite 10 números para a segunda lista: ")
for i in range(5):
    numero = int(input(f"Números {i+1}: "))
    lista2.append(numero)

lista3 = []
for i in range(5):
    lista3.append(lista1[i])
    lista3.append(lista2[i])

print("Lista intercalada: ", lista3)