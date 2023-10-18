#Faça um programa que preencha um matriz 5x5 com números inteiros e exiba o maior valor da matriz e posição que ele se encontra
#Criando a matriz 5x5 preenchida com zeros
matriz = [[0,0,0,0,0],
          [0,0,0,0,0],
          [0,0,0,0,0],
          [0,0,0,0,0],
          [0,0,0,0,0]]
#lendo os valores da matriz
for i in range(5):
    for j in range(5):
        matriz[i][j] = int(input(f"Digite o valor para a posição [{i}][{j}]: "))

#inicialiando a variável do maior valor e sua posição
maior_valor = matriz[0][0]
posicao_maior_valor = (0, 0)
#encontrando o maior valor e sua posição
for i in range(5):
    for j in range(5):
        if matriz[i][j] > maior_valor:
            maior_valor = matriz[i][j]
            posicao_maior_valor = (i, j)
#Exibindo o maior valor e sua posição
print(f"O maior valor da matriz é {maior_valor} e está na posição {posicao_maior_valor}.")





