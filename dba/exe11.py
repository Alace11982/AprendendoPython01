#Atualizando a tabela sem where e com rowcount, metodo que devolve a quantidade de registro alterados
import sqlite3
conexao = sqlite3.connect('agenda.db')
cursor = conexao.cursor()
cursor.execute('''update agenda
                set telefone = '12345-6780' ''')
print("Registros alterados: ", cursor.rowcount)
conexao.commit()
conexao.close()
