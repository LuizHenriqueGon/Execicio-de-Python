#Exercício:
#Um programa que recebe duas notas do aluno e retorna:
#- “Aprovado” se a média das notas for maior ou igual a 6,0;
#- “Reprovado”, se a média for menor que 4,0;
#- “Recuperação” se a média for menor que 6,0, porém, maior que 4,0.
def verificar_nota(nota1, nota2):
    media = (nota1 + nota2) / 2.0

    if media >= 6.0:
        return 'Aprovado'
    elif media < 4.0:
        return'Reprovado'
    else:
        return "Recuperação"

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
resultado = verificar_nota(nota1, nota2)
print(f"Sua média é {((nota1 + nota2) / 2):.2f} e você está {resultado}.")
