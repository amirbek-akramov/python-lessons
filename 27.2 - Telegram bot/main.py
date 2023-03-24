# importing the needed modules

import telebot
from transliterate import to_cyrillic, to_latin

TOKEN = "6220761474:AAEpQB3CY-sVQqbE8nNcm0rMzFCHUd9sm_I" # token for telegram bot
bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=["start"]) # start command for starting
def send_welcome(message): # when start command is writed the welcome text sends
    answer = "Assalomu alykum, xush kelibsiz!" # welcome texts
    answer += "\nBiror nima yozing: "
    bot.reply_to(message, answer) # write and send


@bot.message_handler(func=lambda message: True) # writing messages
def echo_all(message):
    mssg = message.text
    answer = lambda mssg: to_cyrillic(mssg) if mssg.isascii() else to_latin(mssg) # if latin to cyrillic (or reverse)
    bot.reply_to(message, answer(mssg)) # sends message 

bot.polling() # activing the functions
