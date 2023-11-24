#Faça um programa que leia uma palavra e verifique se a mesma é palíndromo(se poder ser lida da mesma for de trás para frente)
#solicita ao usuário que digite uma palavra
palavra = input("Digite ma palavra:")

#inverte a palavra digitada
palavra_invertida = palavra[::-1]

#verifica se a palavra é uma palíndromo
if palavra == palavra_invertida:
    print("A palavra é um palíndromo")
else:
    print("A palavra não é um palíndromo")
    