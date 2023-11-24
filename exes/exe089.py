#Faça um programa que leia um matriz 4x4 e verifique se ela é uma matriz diagonal, isto é, se todos os elmentos for da diagonal principal são iguais a zero
#Lendo os elementos da matriz do usuário
matriz = []
print("Informe os elementos da matriz 4x4:")
for i in range(4):
    linha = []
    for j in range(4):
        elemento = int(input(f"Informe o elemento[{i + 1}] [{j + 1}]: "))
        linha.append(elemento)
    matriz.append(linha)

#verificando se a matriz é diagonal 
e_diagonal = True
for i in range(4):
    for j in range(4):
        if i != j and matriz[i][j] != 0:
            e_diagonal = False
            break

#Exibindo o resultado
if e_diagonal:
    print("A matriz é uma matriz diagonal.")
    for linha in matriz:
        print(linha)
else:
    print("A matriz não é uma matriz diagonal.")

