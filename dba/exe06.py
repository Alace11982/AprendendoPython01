import sqlite3
from contextlib import closing

#usando o with para fechar a conexão com o dados de dados

with sqlite3.connect('agenda.db') as conexao:
    with closing(conexao.cursor()) as cursor:
        cursor.execute('select * from agenda')
        while True:
            resultado = cursor.fetchone()
            if resultado == None:
                break
            print("Nome: %s \nTelefone: %s" % (resultado))


