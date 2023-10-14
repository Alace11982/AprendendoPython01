#Faça um programa que solicite ao usuário umm número e exiba a sequência de Fibonacci até o número informado utilizando um laço de repetição
#programa interessante
n = int(input("Digite um número:"))

a, b = 0, 1

while a <= n:
    print(a, end=" ")
    a, b, = b , a + b
