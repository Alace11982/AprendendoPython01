import random

print('*************************************')
print('*        Jogo da adivinhação        *')
print('*************************************')
print('*            Bem - Vindo            *')

print('*************************************')
print('''Que nivel deseja jogar, digite
      1 - para 20 tentativas, nível facil
      2 - para 10 tentativas, nível médio
      3 - para 5 tentativas, nível díficil''')

while True:    
    nivel = int(input('Qual sua escolha: ', ))
    if nivel == 1:
        total_de_tentativas = 20
        break
    elif nivel == 2:
        total_de_tentativas = 10
        break
    elif nivel == 3:
        total_de_tentativas = 5
        break
    else:
        print("Opção inválida... Escolha 1, 2 ou 3!")   
    print()

numero_secreto = random.randint(1,10)
pontuacao = 1000

print('*************************************')
# Teste print(numero_secreto)
# fazendo com for agora...
for rodada in range(1, total_de_tentativas + 1):
    
    print('Tentativa {} de {}'. format(rodada,total_de_tentativas))
    chute = int(input('Digite o seu número entre 1 a 100: '))
    print('Você digitou: ', chute)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto
    
    if acertou:
        print('Você acertou e fez {} pontos!'.format(pontuacao))
        break
    else:
        if maior:
            print('Você errou! O seu chute foi maior que o número secreto.')
            #print(numero_secreto)
        elif menor:
            print('Você errou! O seu chute foi menor que o número secreto')
            #print(numero_secreto)
        pontos_perdidos = abs(numero_secreto - chute)
        pontuacao = pontuacao - pontos_perdidos

print('Fim do Jogo!\n')