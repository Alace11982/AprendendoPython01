#Deletando algum registro
import sqlite3
conexao = sqlite3.connect('agenda.db')
cursor = conexao.cursor()
cursor.execute("""delete from agenda where nome = 'Maria' """)
print("Registros apagados: ", cursor.rowcount)
if cursor.rowcount ==1:
    conexao.commit()
    print("Alterações gravadas")
else:
    conexao.rollback()
    print("Alteraçoes abortadas")
conexao.close()
