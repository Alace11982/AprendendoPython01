#fazendo uma consulta com Select
import sqlite3
conexao = sqlite3.connect('agenda.db')
cursor = conexao.cursor()
cursor.execute("Select * from agenda where nome = 'Nilo'")
while True:
    resultado = cursor.fetchone()
    if resultado == None:
        break
    print('Nome: %s\nTelefone: %s' % (resultado))
cursor.close()
conexao.close()
