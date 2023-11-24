#Importa o módulo math para utilizar a constante pi
import math

#Solicita ao usuário o valor do raio da esfera
raio = float(input("Digite o valor do raio da esfera:"))

#Calcula o volume de esfera utilizando a formula V = (4/3) * pi * raio 3
volume = (4/3) * math.pi * raio ** 3

#Exibe o resultado do volume da esfera
print("O volume da esfera é: ", volume)
