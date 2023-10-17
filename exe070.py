#Crie um programa que leia um vetor de números inteiros e verifique se todos os elementos são pares
#solictar ao usuário o tamanho do vetor
n = int(input("Informe o tamanho do vetor:"))

#criar vetor vazio
vetor = []

#preencher o vetor com números informados pelo usuário
for i in range(n):
    num = int(input("Digite um número:"))
    vetor.append(num)

#verificar se todos os elementos são pares
todos_pares = True

for num in vetor:
    if num % 2 != 0:
        todos_pares = False
        break

#Exibir o resultado 
if todos_pares:
    print("Todos os elementos são pares.")
else:
    print("Existem elementos ímpares no vetor.")


