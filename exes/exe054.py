#Escreva um program que solicite ao usuário uma frase e exiba a quantidade de vogais na frase
#solicita um frase ao usuário
frase = input('Digite uma frase:')

#inicializa a variável para contar as vogais 
contador_vogais = 0

#percorre cada caractere da frase
for caractere in frase:
    #verifica se o caractere é uma vogal
    #(considerando letras maiúsculas e minúsculas)
    if caractere.lower() in "aeiou":
        contador_vogais += 1
        
#exibe a quantidade de vogais na frase 
print("Quantidade de vogais:", contador_vogais)
