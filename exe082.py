#Faça um programa que preencha um matriz 4x4 com valores aleatórios e exiba a matriz transposta
import random
#Criando a matriz 4x4
matriz = [[0,0,0,0],
          [0,0,0,0],
          [0,0,0,0],
          [0,0,0,0]
          ]
#preenchendo a matriz com valores aleatórios
for i in range(4):
    for j in range(4):
        matriz[i][j] = random.randint(1, 100)

#exibindo a matriz original
print("Matriz Original:")

for linha in matriz:
    for elemento in linha:
        print(elemento, end= '   ')
    print()

#criando a matriz transposta 
matriz_transposta = [[0,0,0,0],
          [0,0,0,0],
          [0,0,0,0],
          [0,0,0,0]
          ]

#preenchendo a matrzi transposta com os elementos da matriz original 
for i in range(4):
    for j in range(4):
        matriz_transposta[i][j] = matriz[j][i]

#exibindo a matriz transposta
print("Matriz Transposta:")
for linha in matriz_transposta:
    for elemento in linha:
        print(elemento, end= "   ")
    print()



