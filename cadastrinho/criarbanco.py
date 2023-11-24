import sqlite3

banco = sqlite3.connect("banco.db")
print("Criando um banco de dados vazio")
cursor = banco.cursor()
cursor.execute("Create table cliente")
