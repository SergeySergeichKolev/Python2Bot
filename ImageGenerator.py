from telebot import TeleBot
import random
import requests

BOTTOKEN = "8204900068:AAGlF9MqLAK4xgBgKZxtG4GE6aM87FhLD2U"

bot = TeleBot(BOTTOKEN) #связь с ботом

@bot.message_handler(commands=['img'])
def sendImg(m):
    #извлекаю то что нужно сгенерить
    bot.reply_to(m, "Генерирую")
    prompt = m.text.partition(' ')[2].strip()
    seed = random.randint(0, 2_000_000_000)
    #просим сгенерить картинку
    url = f"https://image.pollinations.ai/prompt/{prompt}?width=768&height=768&seed={seed}&n=1"
    r = requests.get(url, timeout=90, allow_redirects=True)
    bot.send_photo(m.chat.id, r.content, caption="Готово ✅")


bot.infinity_polling()

