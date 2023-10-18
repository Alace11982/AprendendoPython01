#Faça um programa que leia uma matriz 3x3 e calcule o determinante da matriz.
#lendo a matriz do usuário
matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        elemento = int(input(f'Informe o elemento [{i}] [{j}]:'))
        linha.append(elemento)
    matriz.append(linha)

#exibindo a matriz informada pelo usuário
print("Matriz:") 
for linha in matriz:
    print(linha)

#calculando o determinante 
determinante = (
    matriz [0][0] * matriz[1][1] * matriz[2][2]
    + matriz[0][1] * matriz[1][2] * matriz[2][0]
    + matriz[0][2] * matriz[1][0] * matriz[2][1]
    - matriz[0][2] * matriz[1][1] * matriz[2][0]
    - matriz[0][1] * matriz[1][0] * matriz[2][2]
    - matriz[0][0] * matriz[1][2] * matriz[2][1]
)

#exibindo o determinante 
print(f"Determinante:  {determinante}")



