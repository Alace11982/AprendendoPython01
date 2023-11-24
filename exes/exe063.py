#Escreva um programa que leia um vetor de números inteiros e exiba a média dos elementos.
#Solicita ao usuário os números dos vetor
n =  int(input("Digite a quantidade de números no vetor:"))
vetor = []
for i in range(n):
    num = int(input(f"Digite o número {i+1}:"))
    vetor.append(num)

#calcula a soma dos elementos do vetor
soma = sum(vetor)

#calcula a média dos elementso
media = soma/n

#exibe o resultado
print("A média dos elementos do vetor é:", media)




