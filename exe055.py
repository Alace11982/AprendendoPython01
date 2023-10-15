#Escreva um programa que solicite ao usuário um número inteiro:
num = int(input("Digite um número inteiro:"))

#inicializa a variável divisor com 1
divisor = 1

#percorre os números de 1 a num
while divisor <= num:
    #Verifica se divisor é um divisor de num
    if num % divisor == 0:
        #exibe o divisor
        print(divisor)
    #incrementa o valor de divisor
    divisor += 1



