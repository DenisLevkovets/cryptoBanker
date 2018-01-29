import base
import telebot
import markups
from starter import start_bot, bot


@bot.message_handler(commands=['start'])
def start(msg):
    chat = msg.chat
    bot.send_message(chat.id, "Привет, Мир! Выбери язык", reply_markup=lang())
    # name = chat.first_name
    # if msg.from_user.last_name is not None:
    #     name += chat.last_name
    # base.create_user(chat.id, name, chat.username)


def lang():
    markup = telebot.types.InlineKeyboardMarkup()
    bt_eng = telebot.types.InlineKeyboardButton(text="English", callback_data="langeng")
    bt_rus = telebot.types.InlineKeyboardButton(text="Русский", callback_data="langrus")
    bt_ukr = telebot.types.InlineKeyboardButton(text="Украiнський", callback_data="langukr")
    markup.add(bt_eng)
    markup.add(bt_rus)
    markup.add(bt_ukr)
    return markup


@bot.callback_query_handler(func=lambda call: call.data[:4] == "lang")
def language(call):
    print("1")
    chat = call.message.chat
    bot.send_message(chat.id, "Вы выбрали язык")
    # bot.register_next_step_handler("Вы выбрали язык",confirm)


def confirm(msg):
    markup = telebot.types.ReplyKeyboardMarkup(False, True)
    markup.row("ok")
    bot.send_message(msg.chat.id, "Подтвердить условия", reply_markup=markup)
    bot.register_next_step_handler("ok", welcome)


def welcome(msg):
    bot.send_message(msg.chat.id, "Приветик", reply_markup=markups.welcome())
    bot.edit_message_reply_markup(msg.chat.id, msg.message_id, reply_markup=markups.addWelcome())


if __name__ == "__main__":
    start_bot()
