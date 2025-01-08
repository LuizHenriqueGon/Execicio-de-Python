numeros = []
repete = int(input("Digite quantas vezes repete: "))
for i in range(repete):
    numero1 = float(input('Digite um numero: '))
    numero2 = float(input('Digite outro numero: '))
    numeros.append(numero1%numero2)
print(numeros)