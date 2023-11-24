#Faça um programa que receba uma frase e exiba a quantidade de espaços em brancos presentes na mesma 
#utilizando laço de repetição

frase = input("Digite uma frase:")

#inicializa a variavel contador de espaços em branco

contagem = 0

#percorre cada caractere da frase
for caractere in frase:
    #Verifica se o caractere é um espaço em branco
    if caractere == " ":
        contagem +=1

print("A quantidade de espaços em branco é:", contagem)

