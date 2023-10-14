#Escreva um progrma que solicite ao usuário um lista de números, ate o usuário digitar o número zero, e exiba o maior e menor número da lista
#inicializa as variáveis para o maior e o menor número
maior = float("-inf")
menor = float("inf")

#solicita o primeir número ao usuário
numero = float(input("Digite um número (0 para sair):"))

#enquanto o número digitado for diferente de zero 
while numero != 0:
    #verifica se o número digitado é maior que o maior número encontrado até o momento
    if numero > maior:
        maior = numero
    #verifica se o número digitado é menor que o menor número encontrado até o momento
    if numero < menor:
        menor = numero
    #solicita o próximo número ao usuário
    numero = float(input("Digite um número (0 para sair):"))

#verifica se algum número foi digitado
if maior != float("-inf"):
    #exibe o maior e o menor número da lista
    print("Maior número:", maior)
    print("Menor número:", menor)
else:
    #caso nenhum número tenha sido digitado
    print("Nenhum número foi digitado!")
    