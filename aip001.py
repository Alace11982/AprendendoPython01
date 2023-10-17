import tkinter as tk

def adicionar_numero(numero):
    current = entrada.get()
    entrada.delete(0, tk.END)
    entrada.insert(tk.END, current + str(numero))

def calcular():
    expressao = entrada.get()
    try:
        resultado = eval(expressao)
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, str(resultado))
    except:
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, "Erro")

def limpar():
    entrada.delete(0, tk.END)

# Crie a janela principal
janela = tk.Tk()
janela.title("Calculadora")

# Crie a entrada de texto
entrada = tk.Entry(janela, width=40)
entrada.grid(row=0, column=0, columnspan=4)

# Crie os botões numéricos
botoes_numericos = []
for i in range(1, 10):
    botao = tk.Button(janela, text=str(i), padx=20, pady=10, command=lambda x=i: adicionar_numero(x))
    botao.grid(row=(9 - i)//3 + 1, column=(i - 1) % 3)
    botoes_numericos.append(botao)

# Crie o botão de zero
botao_zero = tk.Button(janela, text="0", padx=20, pady=10, command=lambda: adicionar_numero(0))
botao_zero.grid(row=4, column=1)

# Crie os botões de operação
botoes_operacao = []
operadores = ["+", "-", "*", "/"]
for i in range(len(operadores)):
    botao = tk.Button(janela, text=operadores[i], padx=20, pady=10, command=lambda x=operadores[i]: adicionar_numero(x))
    botao.grid(row=i+1, column=3)
    botoes_operacao.append(botao)

# Crie o botão de igual
botao_igual = tk.Button(janela, text="=", padx=20, pady=10, command=calcular)
botao_igual.grid(row=4, column=2)

# Crie o botão de limpar
botao_limpar = tk.Button(janela, text="C", padx=20, pady=10, command=limpar)
botao_limpar.grid(row=5, column=0)

# Execute a janela
janela.mainloop()