#Escreva um programa que leia dois vetores de números inteiros com o mesmo tamanho e exiba um novo com os elementos resultantes da multiplicação dos elementos correspondentes dos dois vetores
#solicitar ao usuário o tamanho dos vetores
n = int(input("Informe o tamanho dos vetores:"))

#criar vetores vazios
vetor1 = []
vetor2 = []
vetor_resultante = []

#preencher os vetores com números informados pelo usuário
for i in range(n):
    num1 = int(input("Digite um número para o primeiro vetor:"))
    vetor1.append(num1)

    num2 = int(input("Digite um número para o segundo vetor:"))
    vetor2.append(num2)

#Multiplicar os elementos correspondentes dos vetores
for i in range(n):
    multiplicacao = vetor1[i] * vetor2[i]
    vetor_resultante.append(multiplicacao)

#Exibir o vetor resultante
print("O vetor resultante da multiplicação é:", vetor_resultante)






