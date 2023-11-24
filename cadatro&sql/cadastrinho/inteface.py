from tkinter import Tk, Entry, Button
root = Tk()

nome = Entry(root)
cpf = Entry(root)
endereco = Entry(root)

botao_salvar = Button(root, text = 'Salvar')
botao_alterar = Button(root, text = 'Alterar')
botao_remover = Button(root, text = 'Remover')
botao_chupar = Button(root,border=10 )

botao_salvar.pack()
botao_alterar.pack()
botao_remover.pack()
botao_chupar.pack()

nome.pack()
cpf.pack()
endereco.mainloop()
