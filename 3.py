import telebot

TOKEN = '7628595465:AAHgUHi-smK7UE8XayKD8ms_EBTF6PsqV-4'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['text'])
def calculate(message):
    try:
        result = eval(message.text)
        bot.send_message(message.chat.id, f"Ответ: {result}")
    except:
        bot.send_message(message.chat.id, "Ошибка в выражении")

print("Бот запущен")
bot.polling(non_stop=True)