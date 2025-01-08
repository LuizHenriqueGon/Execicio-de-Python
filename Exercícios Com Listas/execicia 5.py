#Faça um Programa que leia 20 números inteiros e armazene-os numa lista.
# Armazene os números pares na lista PAR e os números IMPARES na lista impar.
# Imprima as três listas.
numeros = []
pares = []
impares = []
for i in range(5):
    numero = int(input(f'Digite um numero {i+1}: '))
    numeros.append(numero)
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print("Todos os números: ",numeros)
print("Números pares: ",pares)
print("Números impares: ",impares)