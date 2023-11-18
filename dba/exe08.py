#Fazendo um consulta com conteudo vindo de uma variavel com valor coletado pelo input

import sqlite3
nome = input("Nome a selecionar:")
conexao = sqlite3.connect('agenda.db')
cursor = conexao.cursor()
cursor.execute('Select * from agenda where nome = "%s"' % nome)
while True:
    resultado = cursor.fetchone()
    if resultado == None:
        break
    print("Nome: %s\nTelefone: %s" % (resultado))
cursor.close()
conexao.close()
