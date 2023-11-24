#brincado com valores de lista

lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 12, 3, 3, -52]
#declarando nossa variáveis
maiorValor = lista[0]
menorValor = lista[0]
listaPares = []
ocorrenciasItem1 = 0
mediaElementos = 0
somaNegativos = 0

#iniciando o nosso loop:
for index in range(0,len(lista)):

    #Maior Valor
    if (maiorValor < lista[index]):
        maiorValor = lista[index]
    
    #Menor valor
    if (menorValor > lista[index]):
        menorValor = lista[index]

    #Numeros pares 
    if (lista[index] % 2 == 0):
        listaPares.append(lista[index])-
    
    #Números de ocorrências
    if (lista[index] == lista[0]):
        ocorrenciasItem1 = ocorrenciasItem1 + 1
    
    #Soma dos números negativos
    if (lista[index] < lista[0]):
        somaNegativos = somaNegativos + lista[index]

    #Média do somatório dos elementos
    mediaElementos =+ mediaElementos + lista[index]

mediaElementos = mediaElementos / len(lista)

print("Maior valor: " + str(maiorValor))
print("Menor valor:" + str(menorValor))
print("Lista de elementos pares: " + str(listaPares))
print("Número de ocorrências do primeiro item:" + str(ocorrenciasItem1))
print("Média dos elementos: " + str(mediaElementos))
print("Somatório dos valores negativos:" + str(somaNegativos))

    





