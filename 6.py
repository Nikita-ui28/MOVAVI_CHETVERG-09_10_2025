import telebot

TOKEN = '7628595465:AAHgUHi-smK7UE8XayKD8ms_EBTF6PsqV-4'
bot = telebot.TeleBot(TOKEN)

users = {}

signals = [
    'добавить новую задачу',
    'вывести все задачи',
    'отметить выполненную',
    'математика вычислений'
]


@bot.message_handler(commands=['start'])
def start_handler(message):
    txt = (
        "Привет! Я бот для планирования и отслеживания задач. Для начала работы напиши одну из команд:\n\n"
        "• Добавить новую задачу\n• Вывести все задачи\n• Отметить выполненную\n• Математика вычислений"
    )
    users[message.chat.id] = []
    bot.send_message(message.chat.id, txt)


@bot.message_handler(content_types=['text'])
def handle_message(message):
    txt = message.text.strip().lower()

    if txt in signals:
        if txt == signals[0]:
            bot.send_message(message.chat.id, 'Введите текст задачи')
            bot.register_next_step_handler(message, add_task)

        elif txt == signals[1]:
            show_tasks(message)

        elif txt == signals[2]:
            mark_done(message)

        elif txt == signals[3]:
            bot.send_message(message.chat.id, 'Введите математическое выражение')
            bot.register_next_step_handler(message, math)


def add_task(message):
    task = {
        'task': message.text,
        'done': False
    }
    users[message.chat.id].append(task)
    bot.send_message(message.chat.id, '✅ Задача добавлена')


def show_tasks(message):
    user_id = message.chat.id
    if user_id not in users or not users[user_id]:
        bot.send_message(message.chat.id, '📭 У вас пока нет задач')
        return

    tasks_text = "📋 Ваши задачи:\n\n"
    for i, task in enumerate(users[user_id], 1):
        status = "✅" if task['done'] else "⏳"
        tasks_text += f"{i}. {status} {task['task']}\n"

    bot.send_message(message.chat.id, tasks_text)


def mark_done(message):
    user_id = message.chat.id
    if user_id not in users or not users[user_id]:
        bot.send_message(message.chat.id, '❌ Нет задач для отметки')
        return

    tasks_text = "✅ Введите НОМЕР выполненной задачи:\n\n"
    for i, task in enumerate(users[user_id], 1):
        status = "✅" if task['done'] else "⏳"
        tasks_text += f"{i}. {status} {task['task']}\n"

    bot.send_message(message.chat.id, tasks_text)
    bot.register_next_step_handler(message, process_done_task)


def process_done_task(message):
    user_id = message.chat.id
    if not message.text.isdigit():
        bot.send_message(message.chat.id, '❌ Введите только число!')
        return

    task_num = int(message.text)
    if 1 <= task_num <= len(users[user_id]):
        users[user_id][task_num - 1]['done'] = True
        task_name = users[user_id][task_num - 1]['task']
        bot.send_message(message.chat.id, f'✅ Задача "{task_name}" отмечена выполненной!')
    else:
        bot.send_message(message.chat.id, f'❌ Неверный номер! Введите от 1 до {len(users[user_id])}')


def math(message):
    try:
        result = eval(message.text)
        task_text = f"{message.text} = {result}"

        task = {
            'task': task_text,
            'done': False
        }
        users[message.chat.id].append(task)
        bot.send_message(message.chat.id, f'✅ Результат: {task_text}')
    except:
        bot.send_message(message.chat.id, '❌ Ошибка в выражении')


print('Бот запущен')
bot.polling(
    none_stop=True,
    interval=1
)