import os
import logging
from telegram.ext import CommandHandler, Filters, MessageHandler, Updater
from telegram import ReplyKeyboardMarkup


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)


auth_token = os.getenv('TOKEN')


updater = Updater(token=auth_token)
photo1 = 'IMAG0014.jpg'
photo2 = 'IMAGE_124.jpg'
f = open('hobby.txt')
repoURL='https://github.com/ufo-bat/kids-ai-bot/blob/main/kids_ai.py'


def greet(update, context):
    chat = update.effective_chat
    message_text = update.message.text
    context.bot.send_message(chat_id=chat.id, text='You post '.format(message_text))


def repo(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text=repoURL)


def hobby(update, context):
    chat = update.effective_chat
    about_text = f.read()
    context.bot.send_message(chat_id=chat.id, text=about_text)


def send_photo(update, context):
    chat = update.effective_chat
    text = update.message.text
    if text == "/photo1":
        photo = 'old.jpeg'
    elif text == "/photo2":
        photo = 'young.jpg'
    context.bot.send_document(chat_id=chat.id, document=open(photo, 'rb'))


def send_audio(update, context):
    chat = update.effective_chat
    audio_text = update.message.text
    if audio_text == "/audio1":
        audio = 'GPT.mp3'
    elif audio_text == "/audio2":
        audio = 'SQLnoSQL.mp3'
    elif audio_text == "/audio3":
        audio = 'Love.mp3'
    context.bot.send_audio(chat_id=chat.id, audio=open(audio, 'rb'))


def start(update, context):
    chat = update.effective_chat
    name = update.message.chat.first_name
    button = ReplyKeyboardMarkup([
        ['/photo1', '/photo2'],
        ['/hobby']
    ], resize_keyboard=True)

    context.bot.send_message(
        chat_id=chat.id,
        text='Привет, {}!\n \
            /audio1 - GPT\n \
            /audio2 - SQL\n \
            /audio3 - Love\n \
            /repo - github'.format(name),
        reply_markup=button
    )


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('photo1', send_photo))
updater.dispatcher.add_handler(CommandHandler('photo2', send_photo))
updater.dispatcher.add_handler(CommandHandler('hobby', hobby))
updater.dispatcher.add_handler(CommandHandler('repo', repo))
updater.dispatcher.add_handler(CommandHandler('audio1', send_audio))
updater.dispatcher.add_handler(CommandHandler('audio2', send_audio))
updater.dispatcher.add_handler(CommandHandler('audio3', send_audio))


updater.dispatcher.add_handler(MessageHandler(Filters.text, greet))
updater.dispatcher.add_handler(MessageHandler(Filters.status_update.new_chat_members,
                                                greet))


updater.start_polling()
updater.idle()
