#импортируем модули погоды и API для бота
import pyowm
import telebot

#инициализация
owm = pyowm.OWM('3e77461ec764ac287e2f4cecfad8fe3a')

#токен с сайта для нашего бота
bot = telebot.TeleBot("1097949514:AAFI2co7f5uZJyKTWQuc8n_K6z2vtSn8zjA")

@bot.message_handler(content_types=['text'])
def send_reply(message):
    mgr = owm.weather_manager()
    #принимаем от юзера требуемое место для проверки погоды
    observation = mgr.weather_at_place(message.text)
    w = observation.weather
    #вытаскиваем температуру, тип данных - словарь
    temp = w.temperature('celsius')['temp']
    
    #отдаем ответ
    answer = "В городе " + message.text + " сейчас " + str(temp) + "\n\n"
    answer += "Температура сейчас в районе " + str(temp) + "\n\n"
    
    if temp < 10:
        answer += "Сейчас ппц как холодно, одевайся как танк!"
    elif temp < 20:
        answer += "Холодно, оденься потеплее!"
    else:
        answer += "Температура норм, одевай что угодно."
    bot.send_message(message.chat.id, answer)
    
bot.polling( none_stop = True )