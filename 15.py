import telebot
import random
TOKEN = '7628595465:AAHgUHi-smK7UE8XayKD8ms_EBTF6PsqV-4'
bot = telebot.TeleBot(TOKEN)
numbers = {}
@bot.message_handler(func=lambda message: message.text.lower() == 'начать')
def start_game(message):
    user_id = message.from_user.id
    numbers[user_id] = random.randint(1, 100)
    bot.send_message(message.chat.id, "Я загадал число от 1 до 100. Угадывай!")
@bot.message_handler(func=lambda message: message.text.isdigit())
def check_guess(message):
    user_id = message.from_user.id
    guess = int(message.text)
    if user_id not in numbers:
        bot.send_message(message.chat.id, "Напиши 'начать' чтобы начать игру")
        return
    secret = numbers[user_id]
    if guess == secret:
        bot.send_message(message.chat.id, "Правильно! Ты угадал!")
        del numbers[user_id]
    elif guess < secret:
        bot.send_message(message.chat.id, "Больше")
    else:
        bot.send_message(message.chat.id, "Меньше")
@bot.message_handler(content_types=['text'])
def other_messages(message):
    bot.send_message(message.chat.id, "Напиши 'начать' для начала игры")
print("Бот запущен")
bot.polling(non_stop=True)