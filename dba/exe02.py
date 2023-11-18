#fazendo a consulta em registro no banco de dados
import sqlite3
conexao = sqlite3.connect("agenda.db")
cursor= conexao.cursor()
cursor.execute("Select * from agenda")
resultado = cursor.fetchone()
print("Nome: %s\nTelefone: %s" % (resultado))
cursor.close()
conexao.close()
