#Esta logica esta errada
'''

#Solicita três números ao usuário
num1 = float(input("Digite o primeiro número:"))
num2 = float(input("Digite o segundo número:"))
num3 = float(input("Digite o terceiro número:"))

#Encontra o menor número
if num1 <= num3 and num1 <= num3:
    menor = num1
    if num2 <= num3:
        meio = num2
        maior = num3
    else:
        meio = num3
        maior = num2
elif num2 <= num1 and num2 <= num3:
    menor = num2
    if num1 <= num3:
        meio = num1
        maior = num3
    else:
        meio = num3
        maior = num1
else:
    menor = num3
    if num1 <= num2:
        meio = num1
        maior = num2
    else:
        meio = num2
        maior = num1

#Exibe os números em ordem crescente
print("Os números em ordem crescente são:", menor, meio, maior)

'''

#Solicita três números ao usuário, sem usar as condicionais
num1 = float(input("Digite o primeiro número:"))
num2 = float(input("Digite o segundo número:"))
num3 = float(input("Digite o terceiro número:"))

#Encontra o meno número
menor = min(num1, num2, num3)

#Encontra o maior número
maior = max(num1, num2, num3)

#Calcula o número do meio
meio = num1 + num2 + num3 - maior - menor

#Exibe os números em ordem crescente
print('Os números em ordem crescente são: ', menor, meio, maior)
