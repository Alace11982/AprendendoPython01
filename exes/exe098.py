#Desenvola uma função recursiva para encontrar o menor valor em um vetor
def find_min(v, start, end):
    #Caso base: se o vetor tiver apenas um elemento, retore esse elemento
    if start == end:
        return v[start]
    
    #caso recursivo: encontre o menor valor entre o elemento atual 
    #e o menor valor os elementos restantes
    mid = (start + end) // 2
    left_min = find_min(v, start, mid)
    right_min = find_min(v, mid + 1, end)

    #retorne o menor valor entre o valor encontrado na metade esquerda 
    #e o valor encontrado na metade direita
    return(min(left_min, right_min))

#Escreva uma função recursiva para determinar se uma palavra é um palíndromo
def is_palindrome(word):
    #Caso base: se a palavra tiver 0 ou 1 caractere, é um palíndrom
    if len(word) <= 1:
        return True

    #caso recursivo: verifique se o primeiro é ultimo caractere são iguais
    if word[0] == word[-1]:
        #chame a função recursivamente para o subpalíndromo entre o segundo e penúltimo caractere
        return is_palindrome(word[1:-1])
    else:
        return False

#Testando    
print(is_palindrome('alala'))

#Implemente um função recursiva para calcular a soma dos elementos de um vetor
def sum_elements(arr):
    #caso base: se o vetor estiver vazio, a soma é zero
    if len(arr) == 0:
        return 0

    #caso recursivo: soma o primeiro elemendo com a soma dos elementos restantes
    return arr[0] + sum_elements(arr[1:])

vetor = [1,2,3,4,5]
print(sum_elements(vetor))

