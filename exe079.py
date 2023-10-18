#crie um programa que leia uma palavra e exiba a quantidade de vogais presentes na mesma
palavra = input("Digite uma palavra: ")

#inicializa o contador de vogais 
contagem = 0

#define as vogais
vogais = "aeiouAEIOU"

#percorre cada caractere da palavra
for caractere in palavra:
    #verifca se o caractere é uma vogal
    if caractere in vogais:
        #incrementa o contador de vogais
        contagem += 1

print("A quantidade de vogais na palavra é:", contagem)



