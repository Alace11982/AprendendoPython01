#Utilizando o laço for
#Exibindo os números pares de 1 a 50
print("Números pares de 1 a 50:")
for num in range(2, 51, 2):
    print(num, end =" ")


#Exibindo os números ímpares de 51 a 100
print("\n\nNúmeros ímpares de 51 a 100:")
for num in range(51, 101, 2):
    print(num, end = " ")

#Utilizando o laço wile
#Exibindo os número pares de 1 a 50
print("\n\nNúmeros pares de 1 a 50:")
num_par = 2
while num_par <= 50:
    print(num_par, end = " ")
    num_par += 2

#Exibindo os números ímpares de 51 a 100
print("\n\nNúmeros ímpares de 51 a 100:")
num_impar = 51
while num_impar <= 100:
    print(num_impar, end = " ")
    num_impar += 2

#Exibindo os números pares de 1 a 50 e os número ímpares de 51 a 100
#Utilizando apenas um laço de repetição
print('\n\n')
for num in range(1,101):
    if num <= 50 and num % 2 == 0:
        print(num, "- Par")
    elif num >= 51 and num % 2 != 0:
        print(num, "- Ímpar")
