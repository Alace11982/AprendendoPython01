#Faça um programa que leia um vetor de números inteiros e verifique se ele está em ordem crescente
#leitura do vetor do usuário
vetor = []

n = int(input("Digite o tamanho do vetor:"))

print("Digite os elementos do vetor:")
for i in range(n):
    elemento = int(input(f"Elemento {i+1}:"))
    vetor.append(elemento)

#Verificação se o vetor está em ordem crescente
em_ordem_crescente = True

for i in range(1, n):
    if vetor[i] < vetor[i-1]:
        em_ordem_crescente = False
        break

#Exibição do resultado 
if em_ordem_crescente:
    print("O vetor está em ordem crescente.")
else:
    print("O vetor não está em ordem crescente.")



