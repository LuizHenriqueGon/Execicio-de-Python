#Faça um Programa que leia uma lista de 10 números reais e mostre-os na ordem inversa.
numeros = []

for i in range(10):
    numero = float(input(f"Digite um numero {i+1}: "))
    numeros.append(numero)

print("Os números da ordem inversa: ")
for numero in reversed(numeros):
    print(numero, end=" ")