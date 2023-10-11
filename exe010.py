#Solicita ao usuário para digitar os lados do triângulo
a = float(input("Digite o lado a do triângulo:"))
b = float(input("Digite o lado b do triângulo:"))
c = float(input("Digite o lado c do triângulo:"))

#Solicita ao usuário para digitar a altura relativa ao lado b
h = float(input("Digite a altura relativa ao lado b do triângulo:"))

#Calcula o perímetro do triângulo usando a fórmual p = a + b + c
perimetro = a + b + c

#Calcula a área do triângulo usando a fórmula P = a + b + c
area = (b * h) / 2

#Exibe o resultado do perímetro e da área do triangulo
print("O perímetro do triângulo é:", perimetro)
print("A área do triangulo é", area)
