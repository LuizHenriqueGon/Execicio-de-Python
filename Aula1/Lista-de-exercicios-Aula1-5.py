#Escreva um programa que receba 5 valores e retorne a média entre eles.
Valores = []
for i in range(5):
    Valor = int(input('Digite um valor {i+1}: '))
    Valores.append(Valor)

media = sum(Valores)/len(Valores)

print(f"A média dos valores é: {media}")