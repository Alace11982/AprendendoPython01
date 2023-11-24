#crie um programa que leia um vetor de números inteirso e exiba a soma de todos os elementos
#solicita ao usuário os números do vetor
n = int(input("Digite a quantidade de número no vetor:"))
vetor = []
for i in range(n):
    num = int(input(f'Digite o número {i+1}:'))
    vetor.append(num)

#calcula a soma dos elementos do vetor
soma = 0
for num in vetor:
    soma += num

#exibe o resultado 
print("A soma dos elementos do vetor é:", soma)


