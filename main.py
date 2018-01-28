import base
from starter import start_bot, bot


@bot.message_handler(commands=['start'])
def start(msg):
    chat = msg.chat
    bot.send_message(chat.id, "Привет, Мир!")
    name = chat.first_name
    if msg.from_user.last_name is not None:
        name += chat.last_name
    base.create_user(chat.id, name, chat.username)


if __name__ == "__main__":
    start_bot()
