import sqlite3
import os

os.remove("agenda.db") if os.path.exists('agenda.db') else None

# Criando o banco de dados sqlite3
conexao = sqlite3.connect('agenda.db')

# Criação do objeto cursor que permite trabalhar com comandos sql
cursor = conexao.cursor()

#O método execute é objeto cursor envio o comando SQL ao banco de dados
cursor.execute("create table agenda(nome text,telefone text)")

# Inserindo dados no banco. Operação CRUD.
cursor.execute("insert into agenda (nome,telefone) values (?,?)", ("Juca", "88563-1824"))

#Granvando dados no banco
conexao.commit()
#Executando a leitura de todos os registros da tabela agenda
cursor.execute("select * from agenda")
#Para acessar os dados do comando select, vemos utilizar o
#comando fetchone do cursor. Este método que retorna uma tupla
#como resultado da consulta.
resultado = cursor.fetchone()
#Exibir dados
print("\nNome: %s\nTelefone: %s" % (resultado))

# Inserindo mútiplos registros
# Será utilizado o método executemany.A diferença dele para o comando
#  execute e que executemay trabalho com vários valores.
# Nesse exemplo será utilizada uma lista de tuplas. Cada elementos da lista
#será uma tupla de dois valores
dados = [("João", "98901-0109"),
         ("André", "98902-9800"),
         ("Maria", "98903-9801")]
cursor.executemany("insert into agenda(nome, telefone) values (?,?)", dados)
#Gravando dados
conexao.commit()
# selecionando dados da tabela agenda
cursor.execute("select * from agenda")
# Neste exemplo será utilizado o método fetchall para retornar uma lista
#com o resultado da consulta.
resultado = cursor.fetchall()
conexao.commit()
# Exibindo os dados da lista através do comando for
for registro in resultado:
    print("Nome: %s\nTelefone: %s\n" % (registro))

#Consulta utilizando paremetros
pessoa = input("Entre com o nome a consutar: ")
cursor.execute("select * from agenda where nome = ?", (pessoa,))
x = 0
# Como não sabemos quantos regitros serão retornados, usamos o comando True
# junto com o while
while True:
    consulta = cursor.fetchone()
    if consulta == None:
        if x == 0:
            print("\nNada encontrado!")
        break
    print("Nome: %s\nTelefone: %s\n" % (consulta))
    x += 1
    print("\nQuantidade de registros encontrados =  ", x)

#Alterando Registros
pessoa = input("Entre com o nome da pessoa cujo Telefone será Alterado: ")
telefone = input("Entre como o novo número do telefone: ")
cursor.execute("update agenda set telefone = ? where nome = ?", (telefone, pessoa))
#a atributo rowcount conta a quantidade de linhas afetadas com atualização
if cursor.rowcount == 1:
    conexao.commit()
    print("Alterado Gravadas!")
else:
    #Caso a atualização não seja efetivada, a operação é abortada
    conexao.rollback()
    print("Alterações abortadas!")
cursor.execute("select * from agenda")
dados = cursor.fetchall()
for dado in dados:
    print("Nome: %s\nTelefone: %s\n" % dado)

#Excluindo Registros
pessoa = input("Entre com o nome a ser excluído: ")
cursor.execute("delete from agenda where nome = ?", (pessoa,))
print("Registro Excluídos: ", cursor.rowcount)
if cursor.rowcount == 1:
    conexao.commit()
    print("Alterado Gravadas!")
else:
    conexao.rollback()
    print("\nAlteraçes abortadas!")

cursor.execute("select * from agenda")
for dado in dados:
dados = cursor.fetchall()
    print("Nome: %s\nTelefone: %s\n" % dado)
# fechando o cursor
cursor.close()
#Fechando a conexao com a bonco de dados
conexao.close()