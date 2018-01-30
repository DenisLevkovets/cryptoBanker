import base
import telebot
import markups
from starter import start_bot, bot


@bot.message_handler(commands=['start'])
def start(msg):
    chat = msg.chat
    str = bot.send_message(chat.id, "Привет, Мир! Выбери язык", reply_markup=markups.language())
    welcome(msg)
    # bot.register_next_step_handler(str,language)
    # name = chat.first_name
    # if msg.from_user.last_name is not None:
    #     name += chat.last_name
    # base.create_user(chat.id, name, chat.username)


# def language(msg):
#     chat = msg.chat
#     bot.send_message(chat.id, "Вы выбрали язык")k
#     markup = telebot.types.ReplyKeyboardMarkup(True, True)
#     markup.row("ok")
#     str=bot.send_message(msg.chat.id, "Подтвердить условия", reply_markup=markup)
#     bot.register_next_step_handler(str, welcome)


def welcome(msg):
    bot.send_message(msg.chat.id, "Чат-поддержка", reply_markup=markups.addWelcome())
    bot.send_message(msg.chat.id, "Приветик", reply_markup=markups.welcome())


@bot.callback_query_handler(func=lambda call: call.data == 'currency')
def select_currency(call):
    chat = call.message.chat
    bot.edit_message_text("Валюта", chat.id, call.message.message_id, reply_markup=markups.currency())


@bot.callback_query_handler(func=lambda call: call.data[:4] == 'ccur')
def currency(call):
    current_currency = call.data[4:]  # Выбранная валюта
    chat = call.message.chat
    bot.send_message(chat.id, "Операции покупки или продажи", reply_markup=markups.addWelcome())
    bot.send_message(chat.id, "Здесь совершается операции с людьми", reply_markup=markups.menu())


@bot.callback_query_handler(func=lambda call: call.data == 'backtomenu')
def currency(call):
    chat = call.message.chat
    bot.send_message(chat.id, "Операции покупки или продажи", reply_markup=markups.addWelcome())
    bot.send_message(chat.id, "Здесь совершается операции с людьми", reply_markup=markups.menu())


@bot.message_handler(regexp="Обменные операции")
def exchange(msg):
    bot.send_message(msg.chat.id, "Купить/Продать", reply_markup=markups.exchangeR())
    bot.send_message(msg.chat.id, "Здесь вы совершаете сделки с людьми", reply_markup=markups.exchangeI())


@bot.callback_query_handler(func=lambda call: call.data == 'buy')
def buy(call):
    msg = call.message
    bot.edit_message_text("Покупка валюты", msg.chat.id, msg.message_id, reply_markup=markups.buyI_sellI())


@bot.callback_query_handler(func=lambda call: call.data == 'monero')
def monero(call):
    msg = call.message
    bot.edit_message_text("Покупка/Продажа Monero", msg.chat.id, msg.message_id, reply_markup=markups.payments())


@bot.callback_query_handler(func=lambda call: call.data == 'sell')
def buy(call):
    msg = call.message
    bot.edit_message_text("Продажа валюты", msg.chat.id, msg.message_id, reply_markup=markups.buyI_sellI())


@bot.message_handler(regexp="Кошелёк")
def wallet(msg):
    bot.send_message(msg.chat.id, "Описание кошелька", reply_markup=markups.wallet())


@bot.callback_query_handler(func=lambda call: call.data == 'bringin')
def bring_in(call):
    msg = call.message
    bot.edit_message_text("Выберете валюту на счёт которой придут бабосы", msg.chat.id,
                          msg.message_id, reply_markup=markups.bringin())


@bot.callback_query_handler(func=lambda call: call.data[:6] == 'bbring')
def bbring(call):
    msg = call.message
    bot.edit_message_text("Внесите " + call.data[6:], msg.chat.id, msg.message_id)


@bot.callback_query_handler(func=lambda call: call.data == "my requests")
def user_requests(call):
    bot.send_message(call.message.chat.id, "Если нужно,то просто раскомменти")
    # markup = telebot.types.InlineKeyboardMarkup()
    # data = base.get_user_requests(call.message.chat.id)
    # val = base.get_user_value(call.message.chat.id)
    # if not data:
    #     btn_add = telebot.types.InlineKeyboardButton("📝 Добавить объявление", callback_data='add request')
    #     back = telebot.types.InlineKeyboardButton(text="Назад",
    #                                               callback_data='exchange')
    #     markup.row(btn_add, back)
    #     bot.edit_message_text("У вас нет объявлений", call.message.chat.id, call.message.message_id)
    #     bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id,
    #                                   reply_markup=markup)
    #
    #
    # else:
    #     for each in data:
    #         btn = telebot.types.InlineKeyboardButton(
    #             text=each.rType + ", " + each.paymentMethod + ", " + each.rate + " " + each.currency,
    #             callback_data=each.currency + "->" + each.rid)
    #         markup.row(btn)
    #     btn_add = telebot.types.InlineKeyboardButton("📝 Добавить объявление", callback_data='add request')
    #     back = telebot.types.InlineKeyboardButton(text="Назад",
    #                                               callback_data='exchange')
    #     markup.row(btn_add, back)
    #     bot.edit_message_text("Что-то там про объявления",
    #                           call.message.chat.id, call.message.message_id, parse_mode="markdown")
    #     bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'add request')
def add_request(call):
    bot.send_message(call.message.chat.id, "Выберите валюту", reply_markup=markups.request_curr())


@bot.callback_query_handler(func=lambda call: call.data[:4] == 'rreq')
def req_cur(call):
    cur = call.data[4:]
    msg = call.message
    bot.edit_message_text("Выберите тип объявления", msg.chat.id, msg.message_id, reply_markup=markups.request_type())


@bot.callback_query_handler(func=lambda call: call.data == 'reqsell')
@bot.callback_query_handler(func=lambda call: call.data == 'reqbuy')
def req_buy(call):
    msg = call.message
    ms = bot.send_message(msg.chat.id, "Метод оплаты", reply_markup=markups.pay_method())
    bot.register_next_step_handler(ms, rate)


def rate(msg):
    bot.send_message(msg.chat.id, "Курс")


@bot.message_handler(regexp="Настройки")
def settings(msg):
    bot.send_message(msg.chat.id, "Настройки", reply_markup=markups.settings())


@bot.callback_query_handler(func=lambda call: call.data == "language")
def lang(call):
    chat = call.message.chat
    bot.send_message(chat.id, "Выберите язык", reply_markup=markups.language())


if __name__ == "__main__":
    start_bot()
