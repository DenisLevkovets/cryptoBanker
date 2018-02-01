import base
import telebot
import markups
from starter import start_bot, bot


@bot.message_handler(commands=['start'])
def start(message):
    chat = message.chat
    text = 'Привет, мир!'
    # welcome(msg)
    msg = bot.send_message(chat.id, text, reply_markup=markups.language())
    bot.register_next_step_handler(msg, llanguage)
    # base.create_user(chat.id)


def llanguage(msg):
    chat = msg.chat
    bot.send_message(chat.id, "Вы выбрали язык")
    base.create_user(msg.chat.id, msg.text)
    markup = telebot.types.ReplyKeyboardMarkup(True, True)
    markup.row("ok")
    str = bot.send_message(msg.chat.id, base.get_text(msg.chat.id,"confirm"), reply_markup=markup)
    bot.register_next_step_handler(str, welcome)


def welcome(msg):
    bot.send_message(msg.chat.id, "Чат-поддержка", reply_markup=markups.addWelcome())
    bot.send_message(msg.chat.id, base.get_text(msg.chat.id, 'welcome_inf') % msg.from_user.first_name,
                     reply_markup=markups.welcome(), parse_mode='html')


@bot.callback_query_handler(func=lambda call: call.data == 'currency')
def select_currency(call):
    chat = call.message.chat
    bot.edit_message_text("Валюта", chat.id, call.message.message_id, reply_markup=markups.currency())


@bot.message_handler(regexp="Выбор валюты")
def select_currency(msg):
    chat = msg.chat
    bot.send_message(chat.id, "Валюта", reply_markup=markups.currency())


@bot.callback_query_handler(func=lambda call: call.data[:4] == 'ccur')
def currency(call):
    current_currency = call.data[4:]  # Выбранная валюта
    chat = call.message.chat
    bot.edit_message_text("Операции покупки или продажи\nЗдесь совершается операции с людьми", chat.id,
                          call.message.message_id, reply_markup=markups.menu())


def langg():
    markup = telebot.types.InlineKeyboardMarkup()
    bt_eng = telebot.types.InlineKeyboardButton(text="English", callback_data="langeng")
    bt_rus = telebot.types.InlineKeyboardButton(text="Русский", callback_data="langrus")
    bt_ukr = telebot.types.InlineKeyboardButton(text="Украiнський", callback_data="langukr")
    markup.add(bt_eng)
    markup.add(bt_rus)
    markup.add(bt_ukr)
    return markup


@bot.callback_query_handler(func=lambda call: call.data[:4] == "lang")
def lan(call):
    chat = call.message.chat
    new_lan = call.data[4:]
    bot.edit_message_text( "Вы выбрали язык",chat.id,call.message.message_id)


@bot.callback_query_handler(func=lambda call: call.data == 'requests')
def my_requests(call):
    text = base.get_text(call.message.chat.id, 'no_req')
    bot.edit_message_text(text, call.message.chat.id, call.message.message_id)
    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id,
                                  reply_markup=markups.add_request(call.message.chat.id))



@bot.callback_query_handler(func=lambda call: call.data == 'backtomenu')
def currency(call):
    chat = call.message.chat
    bot.edit_message_text("Операции покупки или продажи\nЗдесь совершается операции с людьми", chat.id,
                          call.message.message_id, reply_markup=markups.menu())


@bot.message_handler(regexp="Назад")
def back(msg):
    bot.send_message(msg.chat.id, "Операции покупки или продажи", reply_markup=markups.addWelcome())
    bot.send_message(msg.chat.id, "Здесь совершается операции с людьми", reply_markup=markups.menu())


@bot.message_handler(regexp="Обменные операции")
def exchange(msg):
    bot.send_message(msg.chat.id, "Купить/Продать", reply_markup=markups.exchangeR())
    bot.send_message(msg.chat.id, "Здесь вы совершаете сделки с людьми", reply_markup=markups.exchangeI())


@bot.callback_query_handler(func=lambda call: call.data == 'buy')
def buy(call):
    chat = call.message.chat
    bot.send_message(chat.id, "Покупка", reply_markup=markups.exchangeR())
    bot.send_message(chat.id, "Выберите валюту", reply_markup=markups.buyI_sellI())


@bot.callback_query_handler(func=lambda call: call.data == 'monero')
def monero(call):
    chat = call.message.chat
    bot.send_message(chat.id, "Покупка/Продажа Monero", reply_markup=markups.payments())


@bot.callback_query_handler(func=lambda call: call.data == 'sell')
def sell(call):
    chat = call.message.chat
    bot.send_message(chat.id, "Продажа", reply_markup=markups.exchangeR())
    bot.send_message(chat.id, "Выберите валюту", reply_markup=markups.buyI_sellI())


@bot.message_handler(regexp="Кошелёк")
def wallet(msg):
    bot.send_message(msg.chat.id, "Кошелёк", reply_markup=markups.exchangeR())
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


@bot.callback_query_handler(func=lambda call: call.data == 'withdraw')
def withdraw(call):
    msg=call.message
    bot.edit_message_text("С какой валюты списать бобосы",msg.chat.id,msg.message_id,reply_markup=markups.withdraw())


@bot.callback_query_handler(func=lambda call: call.data[:5] == 'wwith')
def wwithdraw(call):
    msg=call.message
    bot.edit_message_text("Введите сколько вывести" + call.data[5:],msg.chat.id,msg.message_id)


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
    msg = call.message
    bot.edit_message_text("Выберите валюту", msg.chat.id, msg.message_id, reply_markup=markups.request_curr())


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


@bot.callback_query_handler(func=lambda call: call.data == 'settings')
def setings(call):
    msg = call.message
    bot.edit_message_text("Настройки", msg.chat.id, msg.message_id, reply_markup=markups.settings())


@bot.callback_query_handler(func=lambda call: call.data == "chooselanguage")
def lang(call):
    chat = call.message.chat
    bot.edit_message_text( "Выберите язык",chat.id,call.message.message_id, reply_markup=langg())


@bot.callback_query_handler(func=lambda call: call.data == 'rate')
def rat(call):
    msg = call.message
    bot.edit_message_text("Выберите источник актульного курса", msg.chat.id, msg.message_id,
                          reply_markup=markups.rate())


@bot.callback_query_handler(func=lambda call: call.data[:5] == 'burse')
def burses(call):
    number_of_burse = call.data[5:]
    msg = call.message
    markup = telebot.types.InlineKeyboardMarkup()
    bt_back_to_rates = telebot.types.InlineKeyboardButton(text="Вернуться к выбору биржы", callback_data='rate')
    markup.add(bt_back_to_rates)
    bot.edit_message_text("Для пары BTC/RUB теперь используются котировки биржи ...название...", msg.chat.id,
                          msg.message_id, reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'address')
def address_cur(call):
    msg = call.message
    bot.edit_message_text("Выберите валюту", msg.chat.id, msg.message_id, reply_markup=markups.address())


@bot.callback_query_handler(func=lambda call: call.data[:4] == 'adrs')
def address(call):
    msg = call.message
    mes = bot.edit_message_text("Введите адрес", msg.chat.id, msg.message_id)
    bot.register_next_step_handler(mes, enter_address)


def enter_address(msg):
    new_address = msg
    bot.send_message(msg.chat.id, "Информация сохранена")


if __name__ == "__main__":
    bot.polling()
    # start_bot()
