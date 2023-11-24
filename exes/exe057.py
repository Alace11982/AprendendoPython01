#Faça um programa que determine o máximo divisor comum MDC entre dois números informados pelo usuário
#Solicita ao usuário dois números inteiros
num1 = int(input("Digite o primeiro número inteiro:"))
num2 = int(input('Digite o segundo número inteiro:'))

#inicializa as variáveis a e b com valores de num1 e num2
a = num1
b = num2

#encontra o MDC usando o algoritmo de Euclides
while b != 0:
    resto = a % b
    a = b 
    b = resto

#exibe o resultado 
print("O MDC entre", num1, "e", num2, 'é', a)




