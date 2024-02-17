from telebot import TeleBot

TOKEN_EDHELENA = '6912172227:AAGWPgNrYTq0y_rpTTzLgzc1tPTGX3nv1K4'
edehelenabot = TeleBot(TOKEN_EDHELENA)

@edehelenabot.message_handler(commands=['start','começar'])
def boas_vindas(message):
    edehelenabot.reply_to(message, "Olá, eu sou um bot criado por Estela de Lacerda Oliveira. Estou aqui pra te auxiliar a apr")