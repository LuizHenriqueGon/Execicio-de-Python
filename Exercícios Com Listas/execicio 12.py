#Foram anotadas as idades e alturas de 30 alunos.
# Faça um Programa que determine quantos alunos com mais de 13 anos possuem
# altura inferior à média de altura desses alunos.
idades =[]
alturas = []

for i in range(5):
    idade = int(input(f"Digite a idade do aluno {i + 1}: "))
    altura = int(input(f"Digite a altura do aluno {i + 1}: "))
    idades.append(idade)
    alturas.append(altura)

media_altura = sum(alturas)/len(alturas)

alunos_abaixo_media =0
for i in range(5):
    if idades[i] > 13 and alturas[i] < media_altura:
        alunos_abaixo_media += 1

print(f"Alunos com mais de 13 anos e altura inferior à média: {alunos_abaixo_media}")
