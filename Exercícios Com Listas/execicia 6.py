#Faça um Programa que peça as quatro notas de 10 alunos,
# calcule e armazene numa lista a média de cada aluno,
# imprima o número de alunos com média maior ou igual a 7.0.
medias = []
for i in range(5):
    print(f"Aluno {i+1}:")
    soma_notas = 0
    for j in range(4):
        nota = float(input(f"Nota {j+1}: "))
        soma_notas += nota
    media = soma_notas / 4
    medias.append(media)

alunos_aprovados = [media for media in medias if media >= 7.0]
num_aprovados = len(alunos_aprovados)

print(f"Números de alunos com média maior ou igual a 7.0: {num_aprovados}")