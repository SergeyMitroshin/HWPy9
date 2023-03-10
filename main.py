import telebot
import const
import control

# Создаем экземпляр бота
bot = telebot.TeleBot(const.telergam_token)
# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, const.start_mess)
# Получение сообщений от пользователя
@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, control.parse(message.text))
# Запускаем бота
bot.polling(none_stop=True, interval=0)
