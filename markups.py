import telebot
import base


def language():
    markup = telebot.types.ReplyKeyboardMarkup(True, True)
    markup.row("Engish")
    markup.row("Русский")
    markup.row("Украiньский")
    return markup


def welcome():
    markup = telebot.types.InlineKeyboardMarkup()
    bt_currency = telebot.types.InlineKeyboardButton(text="Выбрать валюту", callback_data="currency")
    bt_buy = telebot.types.InlineKeyboardButton(text="Покупка", callback_data="buy")
    bt_sell = telebot.types.InlineKeyboardButton(text="Продажа", callback_data="sell")
    markup.add(bt_currency)
    markup.add(bt_buy, bt_sell)
    return markup


def addWelcome():
    markup = telebot.types.ReplyKeyboardMarkup(True, False)
    bt_settings = telebot.types.InlineKeyboardButton(text="Настройки")
    bt_service = telebot.types.InlineKeyboardButton(text="О сервисе")
    bt_wallet = telebot.types.InlineKeyboardButton(text="Кошелёк")
    bt_exchange = telebot.types.InlineKeyboardButton(text="Обменные операции")
    markup.add(bt_wallet, bt_exchange)
    markup.add(bt_service, bt_settings)
    return markup


def currency():
    markup = telebot.types.InlineKeyboardMarkup()
    bt_usd = telebot.types.InlineKeyboardButton(text="USD", callback_data="ccurUSD")
    bt_eur = telebot.types.InlineKeyboardButton(text="EUR", callback_data="ccurEUR")
    bt_cny = telebot.types.InlineKeyboardButton(text="CNY", callback_data="ccurCNY")
    bt_rub = telebot.types.InlineKeyboardButton(text="RUB", callback_data="ccurRUB")
    bt_monero = telebot.types.InlineKeyboardButton(text="Monero", callback_data="ccurMonero")
    bt_ripple = telebot.types.InlineKeyboardButton(text="Ripple", callback_data="ccurRipple")
    bt_eos = telebot.types.InlineKeyboardButton(text="EOS", callback_data="ccurEOS")
    bt_btc = telebot.types.InlineKeyboardButton(text="BTC", callback_data="ccurBTC")
    bt_back = telebot.types.InlineKeyboardButton(text="Назад", callback_data="backtomenu")
    markup.add(bt_usd, bt_eur, bt_cny, bt_rub)
    markup.add(bt_monero, bt_ripple, bt_eos, bt_btc)
    markup.add(bt_back)
    return markup


def menu():
    markup = telebot.types.InlineKeyboardMarkup()
    bt_currency = telebot.types.InlineKeyboardButton(text="Выбрать валюту", callback_data="currency")
    bt_buy = telebot.types.InlineKeyboardButton(text="Покупка", callback_data="buy")
    bt_sell = telebot.types.InlineKeyboardButton(text="Продажа", callback_data="sell")
    bt_requests = telebot.types.InlineKeyboardButton(text="Заявки", callback_data="requests")
    bt_auto = telebot.types.InlineKeyboardButton(text="Автопилот", callback_data="auto")
    bt_analyse = telebot.types.InlineKeyboardButton(text="Анализ", callback_data="analyse")
    markup.add(bt_buy, bt_sell)
    markup.add(bt_currency, bt_auto)
    markup.add(bt_requests, bt_analyse)
    return markup


def exchangeI():
    markup = telebot.types.InlineKeyboardMarkup()
    bt_buy = telebot.types.InlineKeyboardButton(text="Покупка", callback_data="buy")
    bt_sell = telebot.types.InlineKeyboardButton(text="Продажа", callback_data="sell")
    bt_requests = telebot.types.InlineKeyboardButton(text="Заявки", callback_data="requests")
    bt_analyse = telebot.types.InlineKeyboardButton(text="Анализ", callback_data="analyse")
    markup.add(bt_buy, bt_sell)
    markup.add(bt_requests, bt_analyse)
    return markup


def exchangeR():
    markup = telebot.types.ReplyKeyboardMarkup(True, False)
    markup.row("Назад", "Выбор валюты")
    markup.row("Настройки", "Кошелёк")
    return markup


def buyI_sellI():
    markup = telebot.types.InlineKeyboardMarkup()
    bt_monero = telebot.types.InlineKeyboardButton(text="Monero", callback_data="monero")
    bt_eos = telebot.types.InlineKeyboardButton(text="EOS", callback_data="eos")
    bt_ripple = telebot.types.InlineKeyboardButton(text="Ripple", callback_data="ripple")
    bt_btc = telebot.types.InlineKeyboardButton(text="BTC", callback_data="btc")
    markup.add(bt_monero, bt_eos)
    markup.add(bt_ripple, bt_btc)
    return markup


def payments():
    markup = telebot.types.InlineKeyboardMarkup()
    bt = telebot.types.InlineKeyboardButton(text="Здесь будут способы оплаты", callback_data="neznau")
    bt_cancel = telebot.types.InlineKeyboardButton(text="Отмена", callback_data="backtomenu")
    markup.add(bt)
    markup.add(bt_cancel)
    return markup


def wallet():
    markup = telebot.types.InlineKeyboardMarkup()
    bt_bring_in = telebot.types.InlineKeyboardButton(text="Внести", callback_data="bringin")
    bt_withdraw = telebot.types.InlineKeyboardButton(text="Вывести", callback_data="withdraw")
    bt_check = telebot.types.InlineKeyboardButton(text="Выписать чек", callback_data="check")
    bt_reports = telebot.types.InlineKeyboardButton(text="Отчёты", callback_data="reports")
    markup.add(bt_bring_in, bt_withdraw)
    markup.add(bt_check, bt_reports)
    return markup


def bringin():
    markup = telebot.types.InlineKeyboardMarkup()
    bt_monero = telebot.types.InlineKeyboardButton(text="Monero", callback_data="bbringMonero")
    bt_eos = telebot.types.InlineKeyboardButton(text="EOS", callback_data="bbringEOS")
    bt_ripple = telebot.types.InlineKeyboardButton(text="Ripple", callback_data="bbringRipple")
    bt_btc = telebot.types.InlineKeyboardButton(text="BTC", callback_data="bbringBitcoin")
    markup.add(bt_monero, bt_eos)
    markup.add(bt_ripple, bt_btc)
    return markup


def withdra():
    markup = telebot.types.InlineKeyboardMarkup()
    bt_monero = telebot.types.InlineKeyboardButton(text="Monero", callback_data="wwithMonero")
    bt_eos = telebot.types.InlineKeyboardButton(text="EOS", callback_data="wwithEOS")
    bt_ripple = telebot.types.InlineKeyboardButton(text="Ripple", callback_data="wwithRipple")
    bt_btc = telebot.types.InlineKeyboardButton(text="BTC", callback_data="wwithBitcoin")
    markup.add(bt_monero, bt_eos)
    markup.add(bt_ripple, bt_btc)
    return markup

def request_curr():
    markup = telebot.types.InlineKeyboardMarkup()
    bt_monero = telebot.types.InlineKeyboardButton(text="Monero", callback_data="rreqMonero")
    bt_eos = telebot.types.InlineKeyboardButton(text="EOS", callback_data="rreqEOS")
    bt_ripple = telebot.types.InlineKeyboardButton(text="Ripple", callback_data="rreqRipple")
    bt_btc = telebot.types.InlineKeyboardButton(text="BTC", callback_data="rreqBitcoin")
    markup.add(bt_monero, bt_eos)
    markup.add(bt_ripple, bt_btc)
    return markup


def request_type():
    markup = telebot.types.InlineKeyboardMarkup()
    bt_buy = telebot.types.InlineKeyboardButton(text="Покупка", callback_data="reqbuy")
    bt_sell = telebot.types.InlineKeyboardButton(text="Продажа", callback_data="reqsell")
    bt_back = telebot.types.InlineKeyboardButton(text="К списку валют", callback_data="add request")
    markup.add(bt_buy, bt_sell)
    markup.add(bt_back)
    return markup


def pay_method():
    markup = telebot.types.ReplyKeyboardMarkup(True, False)
    markup.row("С карты на карту", "Visa", "Сбербанк")
    markup.row("Назад")
    return markup


def settings():
    markup = telebot.types.InlineKeyboardMarkup()
    bt_lan = telebot.types.InlineKeyboardButton(text="Язык", callback_data="chooselanguage")
    bt_rate = telebot.types.InlineKeyboardButton(text="Биржевые курсы", callback_data="rate")
    bt_address = telebot.types.InlineKeyboardButton(text="Адрес", callback_data="address")
    bt_cur = telebot.types.InlineKeyboardButton(text="Выбрать валюту", callback_data="currency")
    bt_auto = telebot.types.InlineKeyboardButton(text="Автопилот", callback_data="auto")
    bt_save = telebot.types.InlineKeyboardButton(text="Безопасный режим", callback_data="savemode")
    markup.add(bt_lan, bt_rate)
    markup.add(bt_address, bt_cur)
    markup.add(bt_auto, bt_save)
    return markup


def add_request(cid):
    markup = telebot.types.InlineKeyboardMarkup()
    text = base.get_text(cid, 'add_req')
    btn = telebot.types.InlineKeyboardButton(text=text, callback_data='add request')
    markup.row(btn)
    return markup


def rate():
    markup = telebot.types.InlineKeyboardMarkup()
    bt_burse1 = telebot.types.InlineKeyboardButton(text="Название биржи 1 ...", callback_data="burse1")
    bt_back_to_settings = telebot.types.InlineKeyboardButton(text="Назад к настройкам", callback_data="settings")
    markup.add(bt_burse1)
    markup.add(bt_back_to_settings)
    return markup


def address():
    markup = telebot.types.InlineKeyboardMarkup()
    bt_monero = telebot.types.InlineKeyboardButton(text="Monero", callback_data="adrsMonero")
    bt_eos = telebot.types.InlineKeyboardButton(text="EOS", callback_data="adrsEOS")
    bt_ripple = telebot.types.InlineKeyboardButton(text="Ripple", callback_data="adrsRipple")
    bt_btc = telebot.types.InlineKeyboardButton(text="BTC", callback_data="adrsBitcoin")
    markup.add(bt_monero, bt_eos)
    markup.add(bt_ripple, bt_btc)
    return markup
