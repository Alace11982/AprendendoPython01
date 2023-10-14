#Escreva um programa que solicite ao usuário um número N e diga se o mesmo é primo o não
import math

numero  = int(input("Digite um número inteiro:"))

if numero < 2:
    print("O número não é primo.")
else:
    eh_primo = True
    limite = math.ceil(math.sqrt(numero))
    for i in range(2, limite+1):
        if numero % i == 0:
            eh_primo = False
            break
    
    if eh_primo:
        print('O numero é primo')
    else:
        print('O número não é primo:')
