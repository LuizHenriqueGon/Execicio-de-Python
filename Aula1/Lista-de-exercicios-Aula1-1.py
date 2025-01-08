#Faça um programa que recebe dois valores e apresente na tela a soma, a subtração e
#multiplicação e a divisão desses dois valores.

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o sengundo número: "))

soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2

if numero2 != 0:
    divisao = numero1 / numero2
else:
    divisao = "Divisão por zero não permitida"

print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")


