import telebot


def poisk(vvod):
    mas=[x for x in open("text_2.txt","r",encoding="utf-8")]
    otvet=["Извините нечего не найдено"]
    vvod1= vvod.lower ()
    vvod2=vvod.upper()
    vvod3=vvod2[0]+vvod1[1:]
    standart_otvet=f"Вот все что мне удалось найти по запросу: {vvod}\n"
    for elem in mas:
        for i in range(len(elem) - len(vvod1)):
            if elem[i:len(vvod1) + i] == vvod1 or elem[i:len(vvod1) + i]==vvod2 or elem[i:len(vvod1) + i]==vvod3:
                if otvet[0]=="Извините нечего не найдено":
                    otvet=[standart_otvet]
                otvet.append((elem))
                break
    return otvet


def soedinenie(a):
    stroc=""
    for i in a :
        stroc+=i+"\n"
    return stroc

# Создаем экземпляр бота
bot = telebot.TeleBot("7354751980:AAGT6-_nosi0LtZVRbV1pqU9nPNQUOSrksA")

# Определяем обработчик сообщений
otvet_na_start="Данный Telegram-бот предназначен для помощи пользователям в поиске и определении различных терминов и понятий. Пользователь может ввести интересующий его запрос, и бот предоставит всю информацию из нашей базы данных \n например введите: макетинг"
@bot.message_handler(func=lambda message: message.text == "/start")
def greet_user(message):
    # Отправляем пользователю приветственное сообщение
    bot.reply_to(message, otvet_na_start)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    # Отправляем пользователю ответное сообщение
    for vivod in poisk(message.text):
        bot.reply_to(message, vivod)


# Запускаем бота
bot.polling()
