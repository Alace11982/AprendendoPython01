import math

#Solicita ao usuário para digitar as três notas
numero1 =float(input("Digite a primeiro número:"))
numero2 =float(input("Digite a segundo número:"))
numero3 =float(input("Digite a terceiro número:"))

#Calcula a média geometrica dos números
media_geometrica = math.pow(numero1 * numero2 * numero3, 1/3)

#Exibe o resultado da média geométrica 
print("A média geométrica dos números é:", media_geometrica)
