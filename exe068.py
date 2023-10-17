#Faça um programa que leia um vetro de números inteiros e exiba quantas vezes um número especifico aparece no vetor
#Solicitar ao usuário o tamanho do vetor
n = int(input("Informe o tamanho do vetor:"))

#criar um vetor vazio
vetor =[]

#preencher o vetor com números informados pelo usuário
for i in range(n):
    num = int(input("Digite um número:"))
    vetor.append(num)

#solicitar ao usuário o número específico a ser pesquisado 
numero = int(input("Digite o número que deseja pesquisar:"))

#inicializar a variárel contador
contador = 0

#verificar cada elemento do vetor
for num in vetor:
    #se o número atual for igual ao número pesquisado, incrementar o contador 
    if num == numero:
        contador += 1

#exibir o resultado
print("O número", numero, "aparece", contador, "vezes no vetor.")




