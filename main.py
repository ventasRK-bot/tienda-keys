import os
import telebot

TOKEN = os.getenv("TOKEN")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "✅ Hola, tu bot está funcionando.")

print("Bot iniciado...")
bot.infinity_polling()
