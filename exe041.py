#Escreva um programa que imprina na tela a tabuada de todos os de 1 a 10
#Loop externo para percorrer os número de 1 a 10
for numero in range (1, 11):
    print("Tabuada do", numero)

    #Loop interno para calcular e imprimir a tabuada do número atual
    for i in range(1, 11):
        resultado = numero * i
        print(numero, "x", i, "=", resultado)

    #imprime um linha em branco após cada tabuada
    print()
