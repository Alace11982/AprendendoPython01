import sqlite3
conexao = sqlite3.connect('agenda.db')
cursor = conexao.cursor()
cursor.execute('''update agenda set telefone = '12345-6789'
               where nome = "Nilo"''')
conexao.commit()
conexao.close()
