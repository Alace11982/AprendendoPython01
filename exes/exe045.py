#Escreve um programa que calcule e exba o valor de potência de um número informado pelo usuário elevado a um expoente também informado pelo usuário, utilizando laços de repetição
#Solicita o número e o expoente ao usuário
numero = int(input("Digite o número base:"))
expoente = int(input("Digite o expoente:"))

#Inicializa a variável para armazenar o resultado da potência 
resultado = 1

#Verifica se o expoente pe positivo, negativo ou zero
if expoente > 0:
    #Calcula a potência usando um laço de repetição
    contador = 0
    while contador < expoente:
        resultado *= numero 
        contador += 1
elif expoente < 0:
    #Calcula a potência inversa usando um laçõ de repetição
    contador =0
    while contador > expoente:
        resultado /= numero 
        contador -= 1

#Exibe o resultado da potência
print('O resultado de ', numero, "elevado a", expoente, "é:", resultado)


