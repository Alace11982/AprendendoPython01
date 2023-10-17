#crie um programa que leia dois vetores de números inteiros com o meesmo tamanho e exiba um novo vetor com a soma dos elementos correspondentes do dois vetores
#leitura dos vetores do usuário
vetor1 = []
vetor2 = []
resultado = []

n = int(input("Digite o tamanho dos vetores:"))
print("Digite os elementos do vetor 1:")
for i in range(n):
    elemento = int(input(f"Elemento {i+1}:"))
    vetor1.append(elemento)
print("Digite os elementos do vetor 2:")
for i in range(n):
    elemento = int(input(f"Elemento {i+1}:"))
    vetor2.append(elemento)

#Calculo da soma dos vetores
for i in range(n):
    soma = vetor1[i] + vetor2[i]
    resultado.append(soma)

#Exibiçaõ do resultado 
print("Resultado da soma dos vetores:", resultado)
