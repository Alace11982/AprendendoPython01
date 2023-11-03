import telebot

CHAVE_API = "6956454280:AAFbU4gnr2uEfPk3WspZEoYVOvikhic11Ug"

bot = telebot.TeleBot(CHAVE_API)

@bot.message_handler(commands=['pizza'])
def pizza(mensagem):
    bot.send_message(mensagem.chat.id, "Saindo a pizza para sua casa: Tempo de espera 20min")

@bot.message_handler(commands=['hamburger'])
def hamburger(mensagem):
    bot.send_message(mensagem.chat.id, 'Saindo o Brabo: em 10 min chega ai')

@bot.message_handler(commands=['salada'])
def salada(mensagem):
    bot.send_message(mensagem.chat.id, "Não tem salada não, clique aqui para iniciar: /iniciar")

@bot.message_handler(commands=['opcao1'])
def opcao1(mensagem):
    texto = """
    O que você quer? (Clique em uma opção)
    /pizza Pizza
    /hamburger Hamburger
    /salada Salada
    """
    bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=['opcao2'])
def opcao2(mensagem):
    bot.send_message(mensagem.chat.id, "Para enviar uma reclamaçao, mande um e-mail para reclamação@blablá.com")

@bot.message_handler(commands=['opcao3'])
def opcao3(mensagem):
    print(mensagem)
    #bot.reply_to(mensagem, "Valeu! Alace mandou um abraço de volta")
    bot.send_message(mensagem.chat.id, "Valeu!Lira mandou um abraço de volta")

def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
    Escolha uma opção para continuar (clique no item):
    /opcao1 Fazer um pedido
    /opcao2 Relamar de um pedido
    /opcao3 Mandar um abraço pro lira
    Responder qualquer outra coisa não vai funcionar, clique em uma das opções
    """
    bot.reply_to(mensagem, texto)

bot.polling()
