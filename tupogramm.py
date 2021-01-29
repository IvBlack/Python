# скрипт для комментирования постов в Телеграмме

from pyrogram import Client  # телеграм клиент
import shelve  # запись информации в файл
import random  # для выбора случайного элеменита из списка
import time  # для выбора случайного элеменита из списка
 
 
# Данные приложения телеграм (можно создать на my.telegram.org)
api_id = .....
api_hash = "......"
phone_number = '+........'  # телефонный номер аккаунта в телеграме
PUBLIC = 'tupogram'  # паблик
# Варианты текстов сообщений
TEXTS = [
    'Круто !',
    'тоже так хочу 😎',
    '5 баллов 👍',
]
COMMENT_EVERY_N = 1  # комментируем каждое N собщение
                     # если равно 1, комментируем каждое сообщение
                     # если равно 3, комментируем каждое третье
                     # если равно 5, комментируем каждое пятое ... итд
 
# список обработанных сообщений
processed_messages = shelve.open('processed_messages.db', writeback=True)
 
# криэйтим клиент телеграма
app = Client(".......", api_id, api_hash,
             phone_number=phone_number)
 
with app:
    public = app.get_chat(PUBLIC)  # ищем паблик по нику
    chat = public.linked_chat  # связанный чат обсуждений паблика
 
    while True:
        for msg in app.get_history(chat.id, limit=100):
            # фильтруем только авторепосты из паблика
            if (msg.from_user is None  # если сообщение не имеет автора
                    # и это репост из паблика (проверка по id)
                    and msg.forward_from_chat.id == public.id):
                if msg.forward_from_message_id % COMMENT_EVERY_N != 0:
                    print(f'Пропускаем message_id={msg.message_id},'
                        f' так как комментируе каждое {COMMENT_EVERY_N}')
                    continue
                # проверяем, есть ли в списке обработанных сообщений этот айди
                # чтобы не комментировать по несколько раз один пост
                if str(msg.forward_from_message_id) in processed_messages:
                    print(f'Пропускаем уже обработанное message_id={msg.message_id}')
                    continue
                # пишем в список обработанных айди этого сообщения
                processed_messages[str(msg.forward_from_message_id)] = True
 
                print(f'Обработка message_id={msg.message_id}')
 
                text = random.choice(TEXTS)  # выбираем случайный текст из списка
                app.send_message(chat.id, text,  # отправляем текст в чат
                                reply_to_message_id=msg.message_id)  # как ответ на сообщение с постом
 
                # для того, чтоб не оставлять больше одного коммента за 5 минут
                break  # выходим из перебора сообщений, если оставили коммент
    time.sleep(60 * 5)
      
# Description

#для начала ставим python 3 и библиотеку pyrogram для связи с телеграммом: команда pip install pyrogram  в терминале. Создаем файл commentator_ez.py И пишем скрипт.
#Импортируем модули: shelve  - создаст файл для инфо, кот будет храниться после закрытия программы, random - Дя выбора случайного элемента из списка.
#Далее - данные для связи с телеграммом, их можно заюзать на my.telegram.org бесплатно. PUBLIC - id паблика, в котором будем писать комменты.
# Список TEXT - для выбора рандомных ответов перед тем, как бот будет комментить пост.
# shelve.open - функция создаст файловую БД, куда будут писаться id откомментированных сбщ, чтобы не комментить дважды одно и то же. processed_messages.db будет создан в дирректории скрипта.
# строкой 30 создадим клиент телеграма через Client с именем "python_cyberpunk" в данном случае /там будет мое имя/, кот запишет данные сессии, дабы не спрашивать у вас пароль в сл/раз. Запишем все в переменную app и передадим блоку with.
# строка 34 - найдем паблик по его id. Можно вывести его на print и посмотреть атрибуты паблика.
# строка 35 - переменная чат содержит связанный чат /атрибут linked_chat переменной public
# строка 38 - перебираем последние 100 сбш в этом СВЯЗАННОМ чате. и следом через вложенный цикл фильтруем только авторепосты из паблика. Далее все крутится в бесконечном цикле while с таймером в конце.
# строка 40 - экспериментально определено, что у авторепостов в атрибумах стоит  - None и forward_from_chat.id == нашему public.id
# строкой 49 проверим есть ли среди среди обработанных сбщ этот Id, и если есть - пропустим, если нет - запишем этот Id  строкой 53 и перейдем к обработке сбщ, оставив коммент.
# для этого запишем в Text случайное сбщ из списка TEXT и строкой 58 отправив сбщ в чат chat.id с текстом text, указав в атрибумах app.send_message айдишник сбщ, на кот хотим ответить в аргументе reply_to_message_id