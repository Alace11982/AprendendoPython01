#Solicita ao usuário para digitar os coeficientes da equação
a = float(input("Digite o coeficiente a:"))
b = float(input("Digite o coeficiente b:"))
c = float(input("Digite o coeficiente c:"))

#Calcula o delta da equação de segundo grau
delta = b**2 - 4*a*c

#Exibe o resultado do delta
print("O delta da equação de segundo grau é:", delta)
