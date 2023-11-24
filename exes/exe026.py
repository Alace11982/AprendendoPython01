#Solicita a idade das três pessoas ao usuário
idade1 = int(input("Digite a idade da primeira pessoa:"))
idade2 = int(input("Digite a idade da segunda pessoa:"))
idade3 = int(input("Digite a idade da terceira pessoa:"))

#Inicializa a variável para contar as pessoas maiores de idade
maiores_de_idade = 0

#Verifica se a primeira pessoa é maior de idade
if idade1 >= 18:
    maiores_de_idade += 1

#Verifica se a segunda pessoa é maior de idadde
if idade2 >= 18:
    maiores_de_idade += 1

#Verifica se a terceira pessoa é maior de idade
if idade3 >= 18:
    maiores_de_idade += 1

#Exibe o resultado 
print("Das três pessoas,", maiores_de_idade, "são maiores de idade.")
