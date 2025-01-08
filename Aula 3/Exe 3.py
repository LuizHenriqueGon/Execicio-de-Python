salario = float(input("Digite o valor do salário: "))
porcentagem_aumento = float(input("Digite a porcentagem de aumento: "))

valor_aumento = salario * (porcentagem_aumento / 100)
novo_salario = salario + valor_aumento

print(f"Valor do aumento: R$ {valor_aumento:.2f}")
print(f"Novo salário: R$ {novo_salario:.2f}")
