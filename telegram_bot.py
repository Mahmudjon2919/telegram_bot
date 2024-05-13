import requests
import telebot

bot = telebot.TeleBot("6586129472:AAE1d2YM_J-qbWA5Ir0CxTqbL69YIlKahjQ"
                      "")

@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.reply_to(message, "Welcome to my Telegram bot!")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

if __name__ == "__main__":
    bot.polling()
