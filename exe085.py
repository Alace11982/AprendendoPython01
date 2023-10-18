#Faça um programa que leia um matriz 3x3 e calcule a média dos valores presentes nas posições pares(soma dos índices par) da matriz
#criando a matriz 3x3 preenchida com zeros
matriz = [[0,0,0],[0,0,0],[0,0,0]]

#lendo os valores da matriz
for i in range(3):
    for j in range(3):
        matriz[i][j] = int(input(f'Digite o valor para posição [{i}][{j}]:' ))

#inicializando o variável da soma e a variável do contador
soma =0 
contador = 0

#calculando a soma dos valores presentes nas posições pares
for i in range(3):
    for j in range(3):
        if (i + j) % 2 == 0:
            
            soma += matriz[i][j]
            contador +=1

            #teste
            #print(i, j, i+j, matriz[i][j], soma, contador, True)

#calculando a média
media = soma / contador

#Exibindo a média dos valores presentes nas posições pares
print(f"A média dos valores presentes nas posições pares da matriz é {media}.")

