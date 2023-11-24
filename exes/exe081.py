#Faça um progrma que preencha um matriz 3x3 com valores informados pelo usuário e exiba a soma dos valores da diagonal principal
#criando a matriz 3x3
matriz = [[0,0,0],
          [0,0,0],
          [0,0,0]]

#preenchendo a matriz com valores informados pelo usuário
for i in range(3):
    for j in range(3):
        matriz[i][j] = int(input(f"Digite o valor para posição [{i}][{j}]: "))

#Exibindo a matriz 
print("Matriz:")
for linha in matriz:
    for elemento in linha:
        print(elemento, end=' ')
    print()

#calculado a soma da diagonal principal
soma_diagonal = 0
for i in range(3):
    
    soma_diagonal += matriz[i][i]
    #teste
    #print(soma_diagonal)
    #print(matriz[i][i])

#exibindo a soma da diagonal principal
print("Soma da diagonal principal: ", soma_diagonal)

