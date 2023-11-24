#Escreva um programa que solicite ao usuário um número N e exiba a soma de todos números de 1 a N
#Solicita ao usuário um número
numero = int(input("Digite um número inteiro:"))

#inicializa a variável de soma 
soma = 0

#Loop para somar os números de 1 a N
for i in range(1, numero + 1):
    soma += i

#Exibe a soma dos números
print("A soma de todos os números de 1 a ", numero, "é:", soma)
