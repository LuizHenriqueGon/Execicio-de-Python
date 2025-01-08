#Faça um Programa que leia uma lista A com 10 números inteiros,
# calcule e mostre a soma dos quadrados dos elementos da lista.
lista_A = []
for i in range(5):
    numero = int(input(f'Digite um numero {i+1}: '))
    lista_A.append(numero)
soma_quadrados = sum([x**2 for x in lista_A])

print("soma dos quadrados dos elementos da lista: ", soma_quadrados)
