import base
import telebot
import markups
from starter import start_bot, bot


@bot.message_handler(commands=['start'])
def start(msg):
    chat = msg.chat
    text = base.get_text('rus', 'welcome')
    bot.send_message(chat.id, text, reply_markup=lang())
    # name = chat.first_name
    # if msg.from_user.last_name is not None:
    #     name += chat.last_name
    base.create_user(chat.id)


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
    base.create_user(chat.id, call.data[4:])
    # bot.register_next_step_handler("Вы выбрали язык",confirm)


@bot.callback_query_handler(func=lambda call: call.data == 'requests')
def my_requests(call):
    text = base.get_text(call.message.chat.id, 'no_req')
    bot.edit_message_text(text, call.message.chat.id, call.message.message_id)
    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id,
                                  reply_markup=markups.add_request(call.message.chat.id))


def confirm(msg):
    markup = telebot.types.ReplyKeyboardMarkup(False, True)
    markup.row("ok")
    bot.send_message(msg.chat.id, "Подтвердить условия", reply_markup=markup)
    bot.register_next_step_handler("ok", welcome)


def welcome(msg):
    bot.send_message(msg.chat.id, "Приветик", reply_markup=markups.welcome())
    bot.edit_message_reply_markup(msg.chat.id, msg.message_id, reply_markup=markups.addWelcome())


if __name__ == "__main__":
    bot.polling()
    # start_bot()
