#Consulta varios registros de forma simplificada

import sqlite3
with sqlite3.connect('agenda.db') as conexao:
    for registro in conexao.execute("select * from agenda"):
        print("Nome: %s\nTelefone: %s" % (registro))

