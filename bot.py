import telebot

# Вставте сюди ваш токен, отриманий від BotFather
TOKEN = '7703988003:AAFeX7KGqenKVEoGQ9SaukJdorENS9zhHr8'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome_message(message):
    bot.send_message(message.chat.id, "Привіт! Це мій бот. Як я можу допомогти?")

# Інші функції для вашого бота

bot.polling()
