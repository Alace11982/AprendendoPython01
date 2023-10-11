import tkinter as tk
from tkinter import messagebox

def exibir_mensagem():
    nome = entrada_nome.get()
    mensagem = f"Olá, {nome}!"
    messagebox.showinfo("Mensagem", mensagem)

# Criação da janela principal
janela = tk.Tk()
janela.title("Programa de saudação")

# Definir o tamanho da janela
largura = 400
altura = 200
janela.geometry(f"{largura}x{altura}")

# Criação dos widgets
label_nome = tk.Label(janela, text="Digite seu nome:")
label_nome.pack()

entrada_nome = tk.Entry(janela)
entrada_nome.pack()

botao_saudacao = tk.Button(janela, text="Exibir saudação", command=exibir_mensagem)
botao_saudacao.pack()

# Execução do loop principal da janela
janela.mainloop()