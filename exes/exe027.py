#Solicita os três númeor ao usuário
lado1 = float(input("Digite o valor do primeiro lado:"))
lado2 = float(input("Digite o valor do segundo lado:"))
lado3 = float(input("Digite o valor do terceiro lado:"))

#Verifica se os lados forman um triângulo
if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    print("Os lados podem formar um triângulo")
else: 
    print("Os lados não podem formar um triângulo")
