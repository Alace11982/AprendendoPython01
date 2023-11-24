#Faça um programa que leia duas matrizes e dê como resposta a multiplicação entre elas. O programa deverá observar se é possível ou não realizar a multiplicação entre as duas matrizes
#Lendo as dimensões das matrizes do usuário
linhas_matriz1 = int(input("Informe o número de linhas da primeira matriz: "))
colunas_matriz1 = int(input("Informe o número de colunas da primeira matriz: "))
linhas_matriz2 = int(input("Informe o número de linhas da segunda matriz:"))
colunas_matriz2 = int(input("Informe o número de colunas da segunda matriz:"))

#verificando se é possível realizar a multiplicação
if colunas_matriz1 != linhas_matriz2:
    print("Não é possível multiplicar as matrizes.")
    print("O número de colunas da primeira matriz deve ser")
    print("igual ao número de linhas da segunda matriz.")
else:
    #Lendo os elementos da primeira matriz
    matriz1 = []
    print("Informe os elementos da primeira matriz:")
    for i in range(linhas_matriz1):
        linha = []
        for j in range(colunas_matriz1):
            elemento = int(input(f"Informe o elemento[{i + 1}][{j +1}]: "))
            linha.append(elemento)
        matriz1.append(linha)

    #Lendo os elementos da segunda matriz
    matriz2 = []
    print("Informe os elementos da segunda matriz:")
    for i in range(linhas_matriz2):
        linha = []
        for j in range(colunas_matriz2):
            elemento = int(input(f"Informe o elemento[{i +1}][{j + 1}]: "))
            linha.append(elemento)
        matriz2.append(linha)

    #Realizando a multiplicação das matrizes
    matriz_resultante = []        
    for i in range(linhas_matriz1):
        linha_resultante = []
        for j in range(colunas_matriz2):
            elemento = 0
            for k in range(colunas_matriz1):
                elemento += matriz1[i][k] * matriz2[k][j]
            linha_resultante.append(elemento)
        matriz_resultante.append(linha_resultante)

    #Exibindo a matriz resultante
    print("Matriz resultante")
    for linha in matriz_resultante:
        print(linha)

