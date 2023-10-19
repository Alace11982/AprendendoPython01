#Escreva uma função recursiva para calcular a potência de um número inteiro elevado a um expoente
def power(base, expoent):
    #Caso base: se o expoente for 0, o resultado é 1
    if expoent == 0:
        return 1
    
    #caso base: se o expoente for 1, o resultado é a própria base
    if expoent == 1:
        return base
    
    #caseo recursivo: dividir o problema em subproblemas menores
    #reduzindo o expoente pela metade a cada chamada recursica
    if expoent % 2 == 0:
        #se o expoente for par, calculamos base^(expoente/2)
        #e elevamos ao quadrado
        sub_result = power(base, expoent // 2)
        return sub_result * sub_result
    else:
        #se o expoente for ímpar, calculamos base^((expoente-1)/2)
        #elevamos ao quadrado e multiplicamos pela base 
        sub_result = power(base, (expoent -1) // 2)
        return sub_result * sub_result * base
    
print(power(2,10))

