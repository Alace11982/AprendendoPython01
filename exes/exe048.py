#Crie um programa que exiba os primeiros N quadrados perfeitos, onde N é informado pelo usuário, utilizando um laço de repetição
N = int(input("Digite um número inteiro N:"))
print("Os primeiros", N, "quadrados perfeitos são:")
count = 0
num = 1

while count < N:
    square = num ** 2
    print(square)
    count += 1
    num += 1
    