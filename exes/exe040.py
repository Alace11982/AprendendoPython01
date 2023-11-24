#Programa tabuada
#Solicitando um número ao usuário
numero = int(input("Digite um número:"))

#Exibindo a tabuada do número digitado 
print("Tabuada do", numero)
for i in range(1, 11):
    resultado = numero * i
    print(numero, "x", i, "=", resultado)


print('\n\n')
#Usando um laço while
c = 1
while c <= 10:
    resultado  = numero * c
    print(numero, 'x', c, "=", resultado)
    c += 1

