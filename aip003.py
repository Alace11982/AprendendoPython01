import sqlite3
import PySimpleGUI as sg

#Esta dando erro porque devo importa a biblioteca PYSIMPLEGUI para o python
#Código feito em inteligência artifical para meramente pratticar meus estudos


# Criar a tabela no banco de dados
def criar_tabela():
    conn = sqlite3.connect('clientes.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            sobrenome TEXT,
            endereco TEXT,
            bairro TEXT,
            cidade TEXT,
            cpf TEXT,
            data_nascimento TEXT,
            telefone_residencial TEXT,
            telefone_contato TEXT,
            whatsapp TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Inserir um novo cliente no banco de dados
def inserir_cliente(cliente):
    conn = sqlite3.connect('clientes.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO clientes (nome, sobrenome, endereco, bairro, cidade, cpf, data_nascimento, telefone_residencial, telefone_contato, whatsapp)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', cliente)
    conn.commit()
    conn.close()

# Atualizar um cliente existente no banco de dados
def atualizar_cliente(cliente):
    conn = sqlite3.connect('clientes.db')
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE clientes SET nome=?, sobrenome=?, endereco=?, bairro=?, cidade=?, cpf=?, data_nascimento=?, telefone_residencial=?, telefone_contato=?, whatsapp=?
        WHERE id=?
    ''', cliente)
    conn.commit()
    conn.close()

# Excluir um cliente do banco de dados
def excluir_cliente(id):
    conn = sqlite3.connect('clientes.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM clientes WHERE id=?', (id,))
    conn.commit()
    conn.close()

# Consultar todos os clientes no banco de dados
def consultar_clientes():
    conn = sqlite3.connect('clientes.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM clientes')
    clientes = cursor.fetchall()
    conn.close()
    return clientes

# Layout da janela
layout = [
    [sg.Text('Nome'), sg.Input(key='nome')],
    [sg.Text('Sobrenome'), sg.Input(key='sobrenome')],
    [sg.Text('Endereço'), sg.Input(key='endereco')],
    [sg.Text('Bairro'), sg.Input(key='bairro')],
    [sg.Text('Cidade'), sg.Input(key='cidade')],
    [sg.Text('CPF'), sg.Input(key='cpf')],
    [sg.Text('Data de Nascimento'), sg.Input(key='data_nascimento')],
    [sg.Text('Telefone Residencial'), sg.Input(key='telefone_residencial')],
    [sg.Text('Telefone de Contato'), sg.Input(key='telefone_contato')],
    [sg.Text('Contato WhatsApp'), sg.Input(key='whatsapp')],
    [sg.Button('Adicionar'), sg.Button('Atualizar'), sg.Button('Excluir'), sg.Button('Sair')],
    [sg.Table(values=[], headings=['ID', 'Nome', 'Sobrenome', 'Endereço', 'Bairro', 'Cidade', 'CPF', 'Data de Nascimento', 'Telefone Residencial', 'Telefone de Contato', 'Contato WhatsApp'], key='table', enable_events=True, justification='left', select_mode='browse')],
]

# Criar a janela
window = sg.Window('Cadastro de Clientes', layout)

# Criar a tabela no banco de dados
criar_tabela()

# Loop de eventos
while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == 'Sair':
        break

    if event == 'Adicionar':
        cliente = (
            values['nome'],
            values['sobrenome'],
            values['endereco'],
            values['bairro'],
            values['cidade'],
            values['cpf'],
            values['data_nascimento'],
            values['telefone_residencial'],
            values['telefone_contato'],
            values['whatsapp']
        )
        inserir_cliente(cliente)

    if event == 'Atualizar':
        selected_row = values['table'][0]
        cliente = (
            values['nome'],
            values['sobrenome'],
            values['endereco'],
            values['bairro'],
            values['cidade'],
            values['cpf'],
            values['data_nascimento'],
            values['telefone_residencial'],
            values['telefone_contato'],
            values['whatsapp'],
            values['table'][selected_row][0]
        )
        atualizar_cliente(cliente)

    if event == 'Excluir':
        selected_row = values['table'][0]
        excluir_cliente(values['table'][selected_row][0])

    # Consultar clientes e atualizar a tabela
    clientes = consultar_clientes()
    window['table'].update(values=clientes)

window.close()