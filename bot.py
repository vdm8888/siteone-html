import telebot

# Ваш токен бота
TOKEN = '7703988003:AAFeX7KGqenKVEoGQ9SaukJdorENS9zhHr8'
bot = telebot.TeleBot(TOKEN)

# ID вашого каналу
CHANNEL_ID = '1002322033269'  # Замість @your_channel_id вставте ваш канал

# Вітальне повідомлення
@bot.message_handler(commands=['start'])
def welcome_message(message):
    bot.send_message(message.chat.id, "Здраствуйте, что бы начать пользоватся ботом нужно подписаться на мой телеграм канал!")

# Перевірка підписки
@bot.message_handler(commands=['check_subscription'])
def check_subscription(message):
    user_id = message.from_user.id

    try:
        # Перевіряємо, чи підписаний користувач на канал
        member = bot.get_chat_member(CHANNEL_ID, user_id)
        
        if member.status in ['member', 'administrator', 'creator']:
            bot.send_message(message.chat.id, "Отлично! Вы подписались на канал, теперь Вам доступны все наши услуги!")
        else:
            bot.send_message(message.chat.id, "Вы не подписаны на канал! Пожалуйста зделайте это!")
    except Exception as e:
        bot.send_message(message.chat.id, "Возникла ошибка при проверке подписки, попробуйте еще раз!")
        print(f"Error: {e}")

# Інші функції для вашого бота (наприклад, для послуг)
@bot.message_handler(commands=['services'])
def services(message):
    bot.send_message(message.chat.id, "Ось доступні послуги:\n1. Послуга 1\n2. Послуга 2\n3. Послуга 3")

# Запуск бота
bot.polling()
