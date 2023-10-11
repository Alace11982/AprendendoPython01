#Lê as notas das duas provas 
nota_prova1 = float(input("Digite a nota da primeira prova:"))
nota_prova2 = float(input("Digite a nota da segunda prova:"))

#Verifica se o aluno foi aprovado ou reprovado em cada prova
if nota_prova1 >= 6:
    print("O aluno foi aprovado na primeira prova.")
else:
    print("O aluno foi reprovado na primeira prova.")

if nota_prova2 >= 6:
    print("O aluno foi aprovado na segunda prova.")
else:
    print("O aluno foi reprovado na segunda prova.")
