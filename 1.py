import telebot

TOKEN = '7628595465:AAHgUHi-smK7UE8XayKD8ms_EBTF6PsqV-4'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Привет! Я простой бот. Мои команды: /start, /help")

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(message.chat.id, "Доступные команды:\n/start - начать\n/help - помощь")

@bot.message_handler(content_types=['text'])
def handle_text(message):
    bot.send_message(message.chat.id, f"Привет, {message.from_user.first_name}! Я бот. Используй /help для списка команд.")

print("Бот запущен")
bot.polling(non_stop=True)