# Inicializa os contadores para cada faixa salarial
faixas_salariais = [0] * 9

# Função para determinar a faixa salarial
def determina_faixa(salario):
    if salario >= 1000:
        return 8
    else:
        return (salario - 200) // 100

# Coletar as vendas brutas dos vendedores
while True:
    vendas_brutas = float(input("Digite as vendas brutas do vendedor (ou -1 para encerrar): "))
    if vendas_brutas == -1:
        break

    salario = 200 + 0.09 * vendas_brutas
    faixa = determina_faixa(salario)
    faixas_salariais[int(faixa)] += 1

# Exibir os resultados
intervalos = [
    "$200 - $299",
    "$300 - $399",
    "$400 - $499",
    "$500 - $599",
    "$600 - $699",
    "$700 - $799",
    "$800 - $899",
    "$900 - $999",
    "$1000 em diante"
]

for i in range(len(faixas_salariais)):
    print(f"{intervalos[i]}: {faixas_salariais[i]} vendedor(es)")
