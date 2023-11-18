
#fazendo um consulta de todos os registros
import sqlite3
conexao = sqlite3.connect('agenda.db')
cursor = conexao.cursor()
cursor.execute('select * from agenda')
resultado=cursor.fetchall()
for registro in resultado:
    print('Nome: %s\nTelefone: %s' % (registro))
cursor.close()
conexao.close()

