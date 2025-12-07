from telebot import TeleBot, types

BOTTOKEN = "8202538559:AAH7fCCHsVhMZ2AdpRRcVvI513PKE89pokg"

bot = TeleBot(BOTTOKEN) #связь с ботом


@bot.message_handler(commands=['start'])
def sf(m):
    bot.send_message(m.chat.id, "Hello")




bot.infinity_polling()






# #при написании команды start бот отправит стикер
# @bot.message_handler(commands=['start'])
# def sendSticer(m):
#     bot.send_sticker(m.chat.id, "CAACAgIAAxkBAAEPeJdo2qHhu_I4sZTH2tzDHWl6pS4p2AACo3wAAov1OUuFmVqEvYjDBTYE")
#

# send_sticker(куда, что)



# @bot.message_handler(commands=['photo'])
# def sf(m):
#     photo = open("image1.jpg", "rb") #извлекаем картинку
#     bot.send_photo(m.chat.id, photo) #отправялем в чат картинку
#     bot.send_message(m.chat.id, "Цена: 1000 руб")
#     bot.send_sticker(m.chat.id, "CAACAgIAAxkBAAEPeJdo2qHhu_I4sZTH2tzDHWl6pS4p2AACo3wAAov1OUuFmVqEvYjDBTYE")
