#Escreva um programa que solicite ao usuário a altura e o raio de um cilindro circular e
# imprima seu volume. Use a fórmula:
# Volume de um cilindro = 3,141592 * raio * raio * altura
PI = 3.141592
Altura = float(input("Digite a Altura do cilindro: "))
Raio = float(input("Digite a Raio do cilindro: "))
Volume = PI * Raio * Raio * Altura
print(f"O volume do cilindro é: {Volume:.2f}")

