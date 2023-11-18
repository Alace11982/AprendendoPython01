#fazendo consulta utilizando parametros
import sqlite3
nome=input("Nome a selecionar: ")
conexão = sqlite3.connect("agenda.db")
cursor = conexão.cursor()
cursor.execute('select * from agenda where nome = ?', (nome,))
x=0
while True:
    resultado = cursor.fetchone()
    if resultado == None:
        if x == 0:
            print('Nada encontrado')
        break
    print('Nome: %s\nTelefone: %s' % (resultado))
    x += 1
cursor.close()
conexão.close()

