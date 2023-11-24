#Faça um program que leia um vetor de números inteiros e exiba o maior elemento presente no vetor
#solicita ao usuário os números do vetor
n = int(input("Digite a quantidade de números no vetor:"))
vetor = []
for i in range(n):
    num = int(input(f'Digite o número {i+1}:'))
    vetor.append(num)

#encontra o maior elemento do vetor
maior = vetor[0]
for num in vetor:
    if num > maior:
        maior = num

#exibe o resultado 
print("O maior elemento do vetor é:", maior)



