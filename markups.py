import telebot
import base

def language():
    markup=telebot.types.ReplyKeyboardMarkup(True,True)
    bt_eng=telebot.types.InlineKeyboardButton(text="English" ,callback_data="langeng")
    bt_rus=telebot.types.InlineKeyboardButton(text="Русский", callback_data="langrus")
    bt_ukr=telebot.types.InlineKeyboardButton(text="Украiнський", callback_data="langukr")
    markup.add(bt_eng)
    markup.add(bt_rus)
    markup.add(bt_ukr)
    return markup


def welcome():
    markup=telebot.types.InlineKeyboardMarkup()
    bt_currency=telebot.types.InlineKeyboardButton(text="Выбрать валюту",callback_data="currency")
    bt_buy=telebot.types.InlineKeyboardButton(text="Покупка",callback_data="buy")
    bt_sell=telebot.types.InlineKeyboardButton(text="Продажа",callback_data="sell")
    markup.add(bt_currency)
    markup.add(bt_buy,bt_sell)
    return markup

def addWelcome():
    markup=telebot.types.ReplyKeyboardMarkup(False,False)
    bt_settings=telebot.types.InlineKeyboardButton(text="Настройки",callback_data="settings")
    bt_service=telebot.types.InlineKeyboardButton(text="О сервисе",callback_data="service")
    bt_wallet=telebot.types.InlineKeyboardButton(text="Кошелёк",callback_data="wallet")
    bt_exchange=telebot.types.InlineKeyboardButton(text="Обменные операции",callback_data="exchange")
    markup.add(bt_wallet,bt_service)
    markup.add(bt_settings)
    markup.add(bt_exchange)
    return markup


def add_request(cid):
    markup = telebot.types.InlineKeyboardMarkup()
    text = base.get_text(cid, 'add_req')
    btn = telebot.types.InlineKeyboardButton(text=text, callback_data='add request')
    markup.row(btn)
    return markup

