#Escreva um programa que receba um nome completo e exiba somente o primeiro nome.
nome_completo = input("Digite o nome completo: ")

#Divindo o nome completo em partes separadas pelo espaço em branco
partes_nome = nome_completo.split()

#obtendo o primeiro nome 
primeiro_nome = partes_nome[0]

print("O primeiro nome é:A", primeiro_nome)

