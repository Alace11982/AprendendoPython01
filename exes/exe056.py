#Faca um programa que determine o menor múltiplo comum MMc entre dois números informados pelo usuário
#solicita ao usuário dois números inteiros 
num1 = int(input("Digite o primeiro número inteiro:"))
num2 = int(input("Digite o segundo número inteiro:"))

#Encontra o maior número entre num1 e num2
maior = max(num1, num2)

#inicialia o valor do MMC como o maior número
mmc = maior

#Verifica se mmc é divisível por num1 e num2
while mmc % num1 != 0 or mmc % num2 != 0:
    #incrementa o valor de mmc pelo maior número
    mmc += maior 

#exibe o resultado 
print("O MMC entre", num1, "e", num2, "é", mmc)