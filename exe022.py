#Lê as notas das duas provas
nota_prova1 = float(input("Digite a nota da primeira prova: "))
nota_prova2 = float(input("Digite a nota da segunda prova:"))

#Calcula a média aritmética simples
media = (nota_prova1 + nota_prova2) / 2

#Verifica se o alono foi aprovado ou reprovado 
if media >= 6:
    print("O aluno foi aprovado. Média: ", media)
else:
    print("O aluno foi reprovado. Média: ", media)


