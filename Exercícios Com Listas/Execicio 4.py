#Faça um Programa que leia uma lista de 10 caracteres, e diga quantas consoantes foram lidas.
# Imprima as consoantes
caracteres = []

for i in range(5):
    caractere = input(f"Digite um caracter {i+1}: ").lower()
    caracteres.append(caractere)

vogais = ['a', 'e', 'i', 'o', 'u']

consoantes = [c for c in caracteres if c.isalpha() and c not in vogais]

num_consoantes = len(consoantes)

print(f"Número de consoantes: {num_consoantes}")
print("Consoantes lidas:", consoantes)
