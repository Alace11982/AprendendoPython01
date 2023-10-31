import random

def imprime_mensagem_abertura():
    print('*************************************')
    print('*           Jogo da Forca           *')
    print('*************************************')
    print('*            Bem -Vindo             *')
    print('*************************************')


def carrega_palavra_secreta():
    arquivo = open('palavras.txt', 'r')
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(lista)
    
    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()

    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    letras_acertadas = ["_" for letra in palavra_secreta]

def pede_chute():
    pass        

def jogar():
    
    imprime_mensagem_abertura()
    
    palavra_secreta = carrega_palavra_secreta()

    #letras_acertadas = ['_','_','_','_','_','_'] ou...
    letras_acertadas = inicializa_letras_acertadas()

    acertou = False
    enforcou = False
    erros = 0

    while(not enforcou and not acertou):
        chute = input('Qual letra?')
        if chute in palavra_secreta:
            posicao = 0
            for letra in palavra_secreta:
                if chute.upper() == letra.upper():
                    letras_acertadas[posicao] = letra
                posicao += 1
        else:
            erros +=1

        enforcou = erros == 3
        acertou = '_' not in letras_acertadas
        print(letras_acertadas)
        
    if(acertou):
        print('Você ganhou!!')
    else:
        print("Você perdeu!!")
    print('Fim do jogo...')

if(__name__ == "__main__"):
    jogar()

