''''''
#Solicita o ano de nascimento ao usuário
ano_nascimento = int(input("Digite o ano de nascimento:"))

#Calcula a idade atual
ano_atual = 2023
idade = ano_atual - ano_nascimento

#Verifica se a pessoa está apta a votar
if idade < 16:
    print("Você não está apto(a) a votar!")
elif idade >=18 and idade <=69:
    print("Você é obrigado (a) a votar.")
else: 
    print("Você está apto(a) a votar, mas não é obrigado(a).")