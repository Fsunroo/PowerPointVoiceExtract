import PowerVextract
import telebot
import time


Token = open('token', 'r').read().strip()
bot = telebot.TeleBot(Token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Hello, ' + message.from_user.first_name + '!')

@bot.message_handler(content_types=['document'])
def extractvoice(message):
    PowerVextract.VoiceExtract(message.document.file_id)
    bot.send_message(message.chat.id, 'Done!')


while True:
    try:
        bot.polling()
    except Exception as e:
        time.sleep(15)