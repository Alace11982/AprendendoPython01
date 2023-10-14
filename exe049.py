#escreva um programa que solicite ao usuário dois números a e b e exiba todos os números entra a e b
A = int(input("Digite o número A:"))
B= int(input("Digite o número B:"))
print("Os números entre", A, "e", B, "são:")

if A <= B:
    for num in range(A, B + 1):
        print(num)
else:
    for num in range(A, B -1, -1):
        print(num)
        5