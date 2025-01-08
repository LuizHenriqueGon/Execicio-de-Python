#Considere o código fonte Python abaixo. (2,0 pontos)
res = [ ]
a, b = 0, 1
n = 100
while a < n:
    valor = a + b
    a, b = b, valor
    res.append(valor)
print (res)
#Para que seja exibido [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# a lacuna I precisa ser preenchida corretamente com o código de
# duas linhas. Desenvolva esse código!
    #valor = a + b
    #res.append(valor)
    #a, b = b, valor