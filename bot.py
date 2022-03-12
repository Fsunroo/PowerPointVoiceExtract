import PowerVextract
import telebot
import time
import os
import shutil

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
    print('extractvoice')
    print(message.chat.id)
    if not os.path.exists(str(message.chat.id)):
        os.mkdir(str(message.chat.id))
    bot.reply_to(message, 'downloading...')
    file_info = bot.get_file(message.document.file_id)
    #bot.send_message(message.chat.id, file_info)
    with open(os.path.join(str(message.chat.id),'file.pptx'), 'wb') as doc:
        doc.write(bot.download_file(file_info.file_path))
    print('downloaded')
    bot.send_message(str(message.chat.id),'extracting...')
    PowerVextract.VoiceExtract(os.path.join(str(message.chat.id),'file.pptx'))
    bot.reply_to(message, 'done!')
    bot.send_message(str(message.chat.id), 'uploading...')
    bot.send_audio(str(message.chat.id), open(os.path.join(str(message.chat.id),'final.mp3'), 'rb'))
    shutil.rmtree(str(message.chat.id))

while True:
    try:
        bot.polling()
    except Exception as e:
        time.sleep(15)