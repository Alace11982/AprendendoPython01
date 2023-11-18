#Consulta de estados brasileiros, ordenado por nome
import sqlite3
conexao = sqlite3.connect("brasil.db")
conexao.row_factory = sqlite3.Row
print("%3s %-20s %12s" % ("Id", "Estado", "Populaçao"))
print("="*37)
#for estado in conexao.execute("select * from estados order by nome desc"):

#for estado in conexao.execute("select * from estados order by populacao"):
#ordem crescente

for estado in conexao.execute("select * from estados order by populacao desc"):
#ordem decrescente
    print("%3s %-20s %12s" %
          (estado['id'],
           estado['nome'],
           estado['populacao']))
conexao.close()
