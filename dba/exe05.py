#consultando registro por registro com fetchone

import sqlite3
conexao = sqlite3.connect('agenda.db')
cursor = conexao.cursor()
cursor.execute("select * from agenda")
while True:
    resultado = cursor.fetchone()
    if resultado == None:
        break
    print("Nome: %s\nTelefone: %s" % (resultado))
cursor.close()
conexao.close()
