print("O meu primeiro programa em python")
print('O meu primeiro programa utilizando aspas simples')
num_int=5
num_dec=7.5
val_str="IFSP"
print("O valor = %f" %num_dec)
print(type(val_str))
print("O valor = ", num_int)
print("O valor = " + str(num_dec))

# comado format
custo = 500
faturamento = 1000
resto = faturamento + custo
print("O faturamento da empresa foi = {} ".format(faturamento))
print("O faturamento da empresa foi = {} e o custo = {}".format(faturamento, custo))
print("O valor = {}".format(resto))

#Comando f string
custo = 1500
faturamento = 5000
lucro = faturamento - custo
print(f"O lucro da empresa foi = {lucro}")
margem = lucro / faturamento
print(f'O margem da empresa foi = {margem}')

#Comando .Nf
custo = 2500
faturamento = 7000
lucro = faturamento - custo
print(f'O lucro da empresa foi de {lucro:,.2f}')
margem = lucro / faturamento
print(f'A margem da empresa foi de {margem:.2%}')