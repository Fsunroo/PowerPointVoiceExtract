import PowerVextract
import telebot
import time


Token = open('token', 'r').read().strip()
print(Token)
bot = telebot.TeleBot(Token)
print('RUNNING...')

@bot.message_handler(commands=['start'])
def start(message):
    print('start')
    bot.send_message(message.chat.id, 'Hello, ' + message.from_user.first_name + '!')

@bot.message_handler(content_types=['document'])
def extractvoice(message):
    bot.reply_to(message, 'downloading...')
    file_info = bot.get_file(message.document.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    PowerVextract.VoiceExtract(downloaded_file)
    bot.reply_to(message, 'done!')
    bot.send_media_group(message.chat.id, ['media.mp3'])

while True:
    try:
        bot.polling()
    except Exception as e:
        time.sleep(15)