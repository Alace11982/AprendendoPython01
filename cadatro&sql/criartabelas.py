import sqlite3

conn = sqlite3.connect("cadastrinho.db")

conn.execute("""CREATE TABLE clientes (
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             nome VARCHAR(100) NOT NULL,
             sexo VARCHAR(1) NOT NULL
             email VARCHAR(100) NOT NULL
             telefone VARCHAR(15) NOT NULL
             cpf VARCHAR(11) NOT NULL)
             """)

# conn.execute("""CREATE TABLE clientes (
#              id INTEGER PRIMARY KEY AUTOINCREMENT,
#              nome VARCHAR(100) NOT NULL,
#              cpf VARCHAR(11) NOT NULL)
#              """)

# conn.execute("""CREATE TABLE clientes (
#              id INTEGER PRIMARY KEY AUTOINCREMENT,
#              nome VARCHAR(100) NOT NULL,
#              cpf VARCHAR(11) NOT NULL)
#              """)

# conn.execute("""CREATE TABLE clientes (
#              id INTEGER PRIMARY KEY AUTOINCREMENT,
#              nome VARCHAR(100) NOT NULL,
#              cpf VARCHAR(11) NOT NULL)
#              """)

# conn.execute("""CREATE TABLE clientes (
#              id INTEGER PRIMARY KEY AUTOINCREMENT,
#              nome VARCHAR(100) NOT NULL,
#              cpf VARCHAR(11) NOT NULL)
#              """)

# conn.execute("""CREATE TABLE clientes (
#              id INTEGER PRIMARY KEY AUTOINCREMENT,
#              nome VARCHAR(100) NOT NULL,
#              cpf VARCHAR(11) NOT NULL)
#              """)

# conn.close()
