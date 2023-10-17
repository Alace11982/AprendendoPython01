#Solicita ao usuário que digite uma frase
frase = input("Digite uma frase:")

#inicializa uma variável para armazenar a frase modificada
frase_modificada = ""

#percorre cada caractere na frase
for caractere in frase:
    #verifica se o caractere é a letra "a"
    if caractere == "a":
        #se for, substitui por "e" e adiciona à frase modificada 
        frase_modificada += "e"
    else:
        #caso contrario, mantém o caractere original
        frase_modificada += caractere

#exibe a frase com as subtituições
print("Frase com as substituições: ", frase_modificada)


