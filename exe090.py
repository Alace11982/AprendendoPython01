#Faça um programa que leia uma matriz m x n, indicando o local onde há minas de um jogo de campo minado(sendo 0 para campo neutro, e 1 para locais onde haveriam minas), e o programa deveria retornar um matriz indicando, para cada posição, o número de minas nas casa vizinhas.
#Lendo as dimensões da matriz
#====Este programa nao entendi nada

M = int(input("Informe o número de linhas da matriz: "))
N = int(input("Informe o número de colunas da matriz:"))

#Lendo os elementos da matriz indicando as minas
matriz = []
print("Informe os elementos da matriz (0 para campo neutro e 1 para mina):")
for i in range(M):
    linha = []
    for j in range(N):
        elemento = int(input(f"Informe o elemento [{i + 1}] [{j + 1}]:"))
        linha.append(elemento)
    matriz.append(linha)

#criando uma matriz auxiliar com zeros
matriz_vizinhas = [[0] * N for _ in range(M)]

#percorrendo a matriz e contando o numero de minas nas casas vizinhas
for i in range(M):
    for j in range(N):
        if matriz[i][j] == 1:
            #incrementando o número de minas nas casas vizinhas
            if i - 1 >= 0 and j - 1 >= 0:
                matriz_vizinhas[i-1][j-1] += 1
            if i - 1 >= 0:
                matriz_vizinhas[i-1][j] += 1
            if i - 1 >= 0 and j + 1 <N:
                matriz_vizinhas[i-1][j+1] += 1
            if j - 1 >= 0:
                matriz_vizinhas[i][j-1] += 1                
            if j + 1 < N:
                matriz_vizinhas[i][j+1] += 1
            if i + 1 < M and j - 1 >= 0:
                matriz_vizinhas[i+1][j-1] += 1
            if i + 1 < M:
                matriz_vizinhas[i+1][j] += 1
            if i + 1 < M and j + 1 < N:
                matriz_vizinhas[i+1][j+1] += 1

#Exibindo a matriz de casas vizinhas com minas
print("Matriz de casas vizinhas com minas:")
for i in range(M):
    for j in range(N):
        print(matriz_vizinhas[i][j], end=" ")
    print()





