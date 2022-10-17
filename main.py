from kiril_to_lotin_translator import to_latin as tl, to_cyrillic as tc

import telebot

bot = telebot.TeleBot("5422864192:AAFfQpQWoA_DJHlY4wMXL1zorCmjlUCNkps", parse_mode=None)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "hello")


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    msg = message.text
    answer = lambda msg: tc(msg) if msg.isascii() else tl(msg)
    bot.reply_to(message, answer(msg))


bot.infinity_polling()
