#crie um programa que leia duas palavras e verifique se segunda palavra é um anagrama da primeira palavra.
word1 = input("Digite a primeira palavra:").lower()
word2 = input("Digite a segunda palavra:").lower()

#remove espaços em branco das palavras
word1 = word1.replace(" ","")
word2 = word2.replace(" ","")

#verifica se as palavras têm o mesmo comprimento
if len(word1) != len(word2):
    print("As palavras não são anagramas.")
    exit()

#converte as palavras em listas de caracteres
word1_list = list(word1)
word2_list = list(word2)

#ordena as listas de caracteres
word1_list.sort()
word2_list.sort()

#Verifica se as listas ordenadas são iguais
if word1_list == word2_list:
    print("A segunda palavra é um anagrama da primeira.")
else:
    print("A segunda palavra não e um anagrama da primeira.")
    


