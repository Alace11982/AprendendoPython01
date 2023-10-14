#Crie um programa que exiba os primeiros N números primos, onde N é informado pelo usuário, utilizando um laçõ de repetição
#programinha legal, gostei
N = int(input("Digite um número inteiro N:"))
print("Os primeiros", N, "números primos são")

count = 0
num = 2
while count < N:
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    
    if is_prime:
        print(count+1, '=> ', num , end=' || ')
        count += 1
    num += 1
    