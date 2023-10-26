#Crie um sistema de perguntas e respostas que interage com o usuário, pedindo que o mesmo insira um resposta. Caso a primeira questão esteja correta, exiba em tela uma mensagem de acerto e parta para a próxima pergunda, caso incorreta, exiba uma mensagem de erro e pule para a próxima pergunta:
#codigo erradaço

'''
base = {
    'Pergunta01':{
        'pergunta':'Quanto e 4 x 4?',
        'alternativa':{'a':12,'b':24,'c':16,'d':20},
        'resposta_certa':'c'
        },
    'Pergunta02':{
        'pergunta':'Quanto e 6 / 3?',
        'alternativas':{'a':2,'b':1,'c':3,'d':4},
        'resposta_certa':'a'
    }}

respostas_certas = 0

for pkeys, pvalues in base.items():
    print(f"{pkeys}:{pvalues['pergunta']}")
    
    for rkeys, rvalues in pvalues['alternativa'].items():
        print(f'[{rkeys}]:{rvalues}')
        
    resposta = input("Escolha uma alternativa [a],[b],[c] ou[d]")

    if resposta == pvalues['resposta_certa']:
        print('Resposta Correta!!!')
        respostas_certas += 1
    else:
        print('Resposta Incorreta!!!')

if respostas_certas ==0:
    print('Você não acertou nenhuma questão.') 
elif respostas_certas ==1:
    print("Você acertou apenas uma questão.")
else:
    print('Você acertou todas as questões')
'''
