#Faça um programa que preencha uma matriz 4x4 com números aleatórios e exiba a soma dos valores presentes em cada linha e em cada coluna.
import random
#criando a matriz 4x4 preenchida com números aleatórios
matriz = [[random.randint(1, 100) for _ in range(4)] for _ in range(4)]

#Exibindo a matriz
print("Matriz: ")
for linha in matriz:
    print(linha)

#Calculando a soma dos valores por linha
somas_linha = []
for linha in matriz:
    soma = sum(linha)
    somas_linha.append(soma)

#Calculando a soma dos valores por coluna
somas_coluna = []
for j in range(4):
    soma = sum(matriz[i][j] for i in range (4))
    somas_coluna.append(soma)

#Exibindo as somas das linhas 
print('Somas por linha:')
for i in range(4):
    print(f"Soma da linha {i + 1}: {somas_linha[i]}")
#Exibindo aas somas das colunas
print("Somas por coluna:")
for j in range(4):
    print(f"Soma da coluna {j+1}: {somas_coluna[j]}")




