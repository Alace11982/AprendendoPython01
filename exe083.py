#Faça um programa qe leia das matrizes 2x2 e exiba a soma das duas matrizes
#Criando as matrizes 2x2 preenchidas com zeros
matriz1 = [[0,0],[0,0]]
matriz2 = [[0,0],[0,0]]
#lendo os valores da primeira matriz
print("Digite os valores da primeira matriz:")
for i in range(2):
    for j in range(2):
        matriz1[i][j] = int(input(f"Digite o valor da posição [{i}][{j}]: "))

#lendo os valores da segunda matriz
print("Digite os valores da segunda matriz:")
for i in range(2):
    for j in range(2):
        matriz2[i][j] = int(input(f"Digite o valor da posição [{i}][{j}]: "))

#criandod a matriz resultado da soma 
matriz_soma = [[0,0],[0,0]]

#calculando a soma das matrizes
for i in range(2):
    for j in range(2):
        matriz_soma[i][j] = matriz1[i][j] + matriz2[i][j]

#Exibindo a matriz soma 
print("Matriz Soma: ")
for linha in matriz_soma:
    for elemento in linha:
        print(elemento, end = " ")
    print()




