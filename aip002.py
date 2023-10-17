#Codigo por i.a.
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
entrada = tk.Entry(janela, width=40, font=("Arial", 14))
entrada.grid(row=0, column=0, columnspan=4)

# Estilização dos botões
botao_estilo = {
    "bg": "#E0E0E0",  # Cor de fundo dos botões
    "fg": "#000000",  # Cor do texto dos botões
    "activebackground": "#BDBDBD",  # Cor de fundo quando o botão está pressionado
    "bd": 0,  # Largura da borda
    "relief": tk.RAISED,  # Estilo da borda
    "padx": 10,  # Espaçamento horizontal
    "pady": 5,  # Espaçamento vertical
    "font": ("Arial", 12)  # Fonte dos botões
}

# Crie os botões numéricos
botoes_numericos = []
for i in range(1, 10):
    botao = tk.Button(janela, text=str(i), command=lambda x=i: adicionar_numero(x), **botao_estilo)
    botao.grid(row=(9 - i)//3 + 1, column=(i - 1) % 3)
    botoes_numericos.append(botao)

# Crie o botão de zero
botao_zero = tk.Button(janela, text="0", command=lambda: adicionar_numero(0), **botao_estilo)
botao_zero.grid(row=4, column=1)

# Crie os botões de operação
botoes_operacao = []
operadores = ["+", "-", "*", "/"]
for i in range(len(operadores)):
    botao = tk.Button(janela, text=operadores[i], command=lambda x=operadores[i]: adicionar_numero(x), **botao_estilo)
    botao.grid(row=i+1, column=3)
    botoes_operacao.append(botao)

# Crie o botão de igual
botao_igual = tk.Button(janela, text="=", command=calcular, **botao_estilo)
botao_igual.grid(row=4, column=2)

# Crie o botão de limpar
botao_limpar = tk.Button(janela, text="C", command=limpar, **botao_estilo)
botao_limpar.grid(row=5, column=0, columnspan=2, sticky="we")

# Execute a janela
janela.mainloop()

#Sinta-se à vontade para ajustar as cores, fontes, tamanhos e outros estilos conforme suas preferências para tornar a calculadora mais agradável aos olhos.