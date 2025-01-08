# Inicializa uma lista para armazenar as notas
notas = []

# Loop para receber as notas do usuário
while True:
    nota = float(input("Digite uma nota (ou -1 para encerrar): "))
    if nota == -1:
        break
    notas.append(nota)

# Mostra a quantidade de valores que foram lidos
quantidade = len(notas)
print(f"Quantidade de valores lidos: {quantidade}")

# Exibe todos os valores na ordem em que foram informados
print("Valores na ordem em que foram informados:", " ".join(map(str, notas)))

# Exibe todos os valores na ordem inversa à que foram informados
print("Valores na ordem inversa:")
for nota in reversed(notas):
    print(nota)

# Calcula e mostra a soma dos valores
soma = sum(notas)
print(f"Soma dos valores: {soma}")

# Calcula e mostra a média dos valores
media = soma / quantidade if quantidade > 0 else 0
print(f"Média dos valores: {media:.2f}")

# Calcula e mostra a quantidade de valores acima da média
acima_media = len([nota for nota in notas if nota > media])
print(f"Quantidade de valores acima da média: {acima_media}")

# Calcula e mostra a quantidade de valores abaixo de sete
abaixo_sete = len([nota for nota in notas if nota < 7])
print(f"Quantidade de valores abaixo de sete: {abaixo_sete}")

# Encerra o programa com uma mensagem
print("Programa encerrado.")
