#Faça um Programa que leia dois listas com 10 elementos cada.
# Gere um terceiro lista de 20 elementos, cujos valores deverão ser compostos
# pelos elementos intercalados dos dois outras listas.
# Altere o programa anterior, intercalando 3 listas de 10 elementos cada.

liste1 = []
lista2 = []
lista3 = []

print("Digite 10 números para a primeira lista")
for i in range(5):
    numero = int(input(f"Número {i+1}: "))
    liste1.append(numero)

print("Digite 10 números para a segunda lista")
for i in range(5):
    numero = int(input(f"Número {i+1}: "))
    lista2.append(numero)
print("Digite 10 números para a terceira lista")
for i in range(5):
    numero = int(input(f"Número {i + 1}: "))
    lista3.append(numero)

lista4 = []
for i in range(5):
    lista4.append(liste1[i])
    lista4.append(lista2[i])
    lista4.append(lista3[i])

print("Lista intercalada: ", lista4)