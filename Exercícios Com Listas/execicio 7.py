#Faça um Programa que leia uma lista de 5 números inteiros, mostre a soma,
# a multiplicação e os números.
numeros = []
for i in range(5):
    numero = int(input(f'Digite um numero {i+1}: '))
    numeros.append(numero)
soma = sum(numeros)

multiplicacao = 1
for numero in numeros:
    multiplicacao *= numero

print("Números inseridos:", numeros)
print("Soma dos números:", soma)
print("Multiplicação dos números:", multiplicacao)