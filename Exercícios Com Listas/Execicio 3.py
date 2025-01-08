#Faça um Programa que leia uma lista de 4 notas, mostre as notas e a média na tela.
notas = []
for i in range(5):
    nota = float(input('Digite a nota: '))
    notas.append(nota)

media = sum(notas) / len(notas)

print("Notas inseridas")
for i in range(5):
    print(notas[i], end=' ')

print(f"\nA média das notas é: {media:.2f}")
