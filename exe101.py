#Escreva um programa que solicite ao usuário uma frase e exiba a frase de trás para frente
#Solicita um frase ao usuário
frase = input("Digite um frase: ")

#inicializa a variável de controle 
indice = len(frase) -1

#inicializa a variável para armazenar a frase invertida
frase_invertida = ""

#enquanto o índice for válido
while indice >= 0:
    #concatena o caractere atual na frase invertida
    frase_invertida += frase[indice]
    #decrementa o índice 
    indice -= 1

#Outra maneira de inverter a frase
#frase_invertida = frase[::-1]

#Exibe a frase invertida
print("Frase invertida: ", frase_invertida)


