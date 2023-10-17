#crie um programa qe leia um vetor de números inteiros e encontre o segundo maior elemento presente no vetor
#solicitar ao usuário o tamanho do vetor
n = int(input("informe o tamanho do vetor:"))

#criar um vetor vazio
vetor = []

#preencher o vetor com números informados pelo usuário
for i in range(n):
    num = int(input("Digite um número: "))
    vetor.append(num)

#encontrar o maior elemento do vetor
maior = max(vetor)

#inicializar a variável que irá armazenar o segundo maior elemento
segundo_maior = float('-inf')

#verificar cada elemento do vetor
for num in vetor:
    #verificar se o número é menor que o maior elemento
    #e maior que o segundo maior elemento
    if num < maior and num > segundo_maior:
        segundo_maior = num

#Exibir o segundo maior elemento
print('O segundo maior elemento é:', segundo_maior)
