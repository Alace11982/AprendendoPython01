#escreva um programa que receba um nome completo e exiba o sobrenome(último nome) primeiro
nome_completo = input("Digite o nome completo:")

#divide o nome completo em partes separadas pelo espaço em branco 
partes_nome = nome_completo.split()

#obtem o último nome
sobrenome = partes_nome[-1]

print("O sobrenome é:", sobrenome)

