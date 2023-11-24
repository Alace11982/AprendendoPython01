#Escreva um programa que leia números do usuário até que seja digitado un número negativo, e exiba a soma dos números positivos
soma = 0

while True:
    numero = int(input("Digite um número (negativo pra encerrar):"))

    if numero  < 0:
        break

    if numero >= 0:
        soma += numero

print("A soma dos números positivos é:", soma)