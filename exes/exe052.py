#Escreva um programa que leia números do usuário até que seja digitado zero, e exiba a média dos números digitados.
#inicializa a variável de soma e contador
soma = 0
contador = 0

#solicita o primeiro número ao usuário
numero = float(input("Digite um número (0 para sair):"))

#Enquanto o número digitado for diferente de zero
while numero != 0:
    #Adiciona o número à soma
    soma += numero
    #incrementa o contador 
    contador += 1
    #solicita o próximo número ao usuário
    numero = float(input('Digite um número (0 para sair):'))

#Verifica se foram digitados números 
if contador > 0:
    #calcula a média
    media = soma / contador
    #exibe a média dos números digitados 
    print("A média é:", media)
else:
    #caso nenhum número tenha sido digitado
    print("Nenhum número foi digitado!")




