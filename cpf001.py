#Simples código para validação de cpf, que eu não entendi nada kkkk

#Faça um programa que solicite o CPF do usuário e então faça a validação do mesmo 
#Solicita ao usuário o CPF
cpf = input("Digite o CPF (somente números):")

#verifica se o CPF possui 11 dígitos
if len(cpf) != 11:
    print("CPF inválido. O CPF deve conter 11 dígitos.")
else:
    #Verifica se todos os dígitos são iguais (CPF inválido)
    if cpf == cpf[0] * 11:
        print("CPF inválido. Todos os dígitos são iguais.")
    else:
        #verifica os dígitos verificadores
        cpf = [int(digito) for digito in cpf] #converte o CPF em um lista de dígitos
        #calcula o primeiro dígito verificador
        soma = sum(digito * (10 - posicao) for posicao, digito in enumerate(cpf[:9]))
        resto = soma % 11
        if resto < 2:
            digito_verificador1 = 0
        else:
            digito_verificador1 = 11 - resto
        #verificar o primeiro dígito verificador
        if cpf[9] != digito_verificador1:
            print("CPF inválido. Primeiro dígito verificador incorreto.")
        else:
            #Calcula o segundo dígito verificador 
            soma = sum(digito * (11 - posicao) for posicao, digito in enumerate(cpf[:10]))
            resto = soma % 11
            if resto < 2:
                digito_verificador2 = 0
            else:
                digito_verificador2 = 11 - resto
            #verifica o segundo dígito verificador
            if cpf[10] != digito_verificador2:
                print("CPF inválido. Segundo digito verificador incorreto.")
            else:
                print("CPF válido.")



    



