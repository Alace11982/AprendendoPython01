#INCOMPLETO
##########################


#Inplemnete um funçaõ recursiva para calcular a sequência de Fibonacci até um determinado número
def fibonacci(n):
    #Casos base Fibonacci de 0 é 0 e de 1 é 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    #Chamada recursiva para calcular a sequência de Fibonacci
    else:
        return fibonacci(n-1) + fibonacci(n-2)
   

#Escreva um funçao recursiva para calcular o fatorial de um número
def fatorial(n):
    #caso base: fatorial de 0 ou 1 é 1
    if n ==0 or n == 1:
        return 1
    #Chamada recurvisa para calcular o fatorial
    else:
        return n * fatorial(n-1)
    

#Crie uma funçao recursiva para verificar se um número é primo
def is_prime(n, divisor = 2):
    #Casos base
    if n <= 1:
        return False
    elif divisor * divisor > n:
        return True
    elif n % divisor == 0:
        return False
    #Chamada recurvisa
    else:
        return is_prime(n, divisor + 1)
    
#Testando número primo
print(is_prime(11))
