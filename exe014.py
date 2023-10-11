#Importa o módulo math para utilizar a função sqrt (raiz quadrade)
import math

#Solicita ao usuario as coordenadas do primeiro ponto 
x1 = float(input("Digite a coordenada x do primeiro ponto: "))
y1 = float(input("Digita a coordenada y do primeiro ponto: "))

#Solicita ao usuario as coordenadas do segundo ponto 
x2 = float(input("Digite a coordenada x do segundo ponto: "))
y2 = float(input("Digita a coordenada y do segundo ponto: "))

#Calcula a diferença entre as coordenadas x e y do dois pontos 
dif_x = x2 - x1
dif_y = y2 - y1

#Calcula a distância entre os pontos utilizando o teorema de Pitágoras
distancia = math.sqrt(dif_x ** 2 + dif_y ** 2)

#Exibe o resultado da distância entre os pontos
print("A distância entre os pontos é: ", distancia)


