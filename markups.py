import telebot

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
    markup.add(bt_settings)
    return markup

