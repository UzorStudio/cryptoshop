import telebot as telebot
from telebot import types
from tronpy import Tron
from tronpy.providers import HTTPProvider

import base

db = base.BaseShop("localhost")
client = Tron(HTTPProvider(api_key="3fdadf50-c0e0-4223-ae9c-00fc44ff6358"),network="shasta")


bot = telebot.TeleBot('5072194047:AAFeQRpZAloSxWP6iX2sOLKZ5suXZ_qRL2I')

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    keyboard.add(types.KeyboardButton(text="Читы"))
    keyboard.add(types.KeyboardButton(text="Баги"))
    print(db.getUsr(message.chat.id))

    if db.getUsr(message.chat.id) == None:
        txt = "Id: "+str(message.chat.id)+"\n"+"balance: "+str(0)+"\n"+"cart: "+"none"

        acc = client.generate_address()
        if db.getAllUsr() == []:
            keyboard = types.InlineKeyboardMarkup()
            keyboard.add(types.InlineKeyboardButton(text="Добавить товар", callback_data="add prod"))
            keyboard.add(types.InlineKeyboardButton(text="Удалить товар", callback_data="dell prod"))

            db.regUser(message.chat.id, acc["base58check_address"], acc["private_key"], "usr")
            bot.send_message(message.chat.id, "What ar u wont?", reply_markup=keyboard)

        else:
            db.regUser(message.chat.id,acc["base58check_address"],acc["private_key"],"usr")
            bot.send_message(message.chat.id,txt,reply_markup=keyboard)

    else:
        usr = db.getUsr(message.chat.id)
        txt = "Id: " + str(usr["usrId"]) + "\n" + "balance: " + str(usr["balance"]) + "\n" + "cart: " + str(usr["cart"])
        bot.send_message(message.chat.id, txt, reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def text(message):
    if message.text == "Читы":
        pass
    if message.text == "Баги":
        pass

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    print(call.message)
    if call.message:
        if call.data == "add prod":



bot.polling(none_stop=True)