#Faça um programa que calcule e exiba a soma do números pares de 1 a 100 utilizando um laço de repetição
#Inicializa a variável de soma 
soma  = 0
#Utiliza um laço de repetição para percorrer os números de 1 a 100
for numero in range(1,100):
    #Verifica se o número é par
    if numero % 2 == 0:
        #Se for par, adiciona o número à soma 
        soma += numero

#Exibe a soma dos númros pares
print("A soma dos números pares de 1 até 100 é:", soma)

#########################################################
#uma maneira diferente de resolver
soma = 0
#Utiliza um laço de repetição para percorrer os números ares de 1 a100 
for numero in range(2,101,2):
    #Adiciona o número à soma 
    soma += numero 

#Exibe a soma dos números pares
print("A soma dos números pares de 1 a 100 é: ", soma)
