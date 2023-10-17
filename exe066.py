#escreva um programa que leia um vetor de números inteiros e exiba os elementos na ordem inversa
#Leitura do vetor do usuário
vetor = []

n= int(input("Digite o tamanho do vetor:"))

print("Digite os elementos do vetor:")
for i in range(n):
    elemento = int(input(f"Elemento {i+1}:"))
    vetor.append(elemento)

#exibição dos elementos na ordem inversa
print("Vetor na ordem inversa:")
for i in range(n-1, -1, -1):
    print(vetor[i])
    

