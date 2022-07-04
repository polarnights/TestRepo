import telebot
import requests
from telebot import types

token = '5406309028:AAEW7yQajJqmSR7M9vA0pjEwT2AHLZRK1Dg'
bot = telebot.TeleBot(token)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/start":
        bot.send_message(message.chat.id,
                         "Добрый день!  В компании Теремок сейчас открыта позиция Повар-кассир в г. Москва. Если вакансия интересна, то дальше мы расскажем об условиях работы.")
        keyboard = types.InlineKeyboardMarkup()
        key_yes = types.InlineKeyboardButton(text='Да', callback_data='Success1')
        keyboard.add(key_yes)
        key_no = types.InlineKeyboardButton(text='Нет', callback_data='Refuse1')
        keyboard.add(key_no)
        bot.send_message(message.from_user.id, text='Интересна ли вам вакансия?', reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "Success1":
        photo = open('test_starting_pic.jpeg', 'rb')
        keyboard = types.InlineKeyboardMarkup()
        key_yes = types.InlineKeyboardButton(text='Да', callback_data='Success2')
        keyboard.add(key_yes)
        key_no = types.InlineKeyboardButton(text='Нет', callback_data='Refuse2')
        keyboard.add(key_no)
        bot.send_message(call.message.chat.id, text="Отлично! Мы предлагаем:\nЗ/П от 49 000 до 82 000 руб., всегда есть подработка.\nРаботу рядом с домом.\nГрафик работы на выбор: 3/3; гибкий от 6 часов в день; вахта – 20/10 или 30/10.\nКомпенсацию проживания в общежитии в размере 9 000 руб., или ЖКХ до 5 000 руб.\nОплата проезда в первый месяц работы.\nОплата проезда из региона до Москвы по факту предоставления именного билета.\nПомощь в оформлении мед. книжки.\nБесплатное, вкусное и полезное питание, комфортная спецодежда.\nКарьерный рост до Администратора ресторана.\n", photo=photo)
        bot.send_message(call.message.chat.id, text="Что нужно делать:\nЗаниматься приготовлением блюд русской кухни.\nПриветствовать гостя, помогать в выборе блюд, расчитывать его на кассе.\n")
        bot.send_message(call.message.chat.id, text="Рассматриваем без опыта работы, предусмотрено бесплатное обучение, стипендия 15000 руб.\n")
        bot.send_message(call.message.chat.id, text="Устраивают ли вас предложенные условия?\n", reply_markup=keyboard)

    if call.data == "Success2":
        bot.send_message(call.message.chat.id, text="Ответьте на 2 вопроса, чтобы узнать вас получше.\n")
        keyboard = types.InlineKeyboardMarkup()
        key_age1 = types.InlineKeyboardButton(text='Младше 18 лет', callback_data='BadAge')
        keyboard.add(key_age1)
        key_age2 = types.InlineKeyboardButton(text='От 18 до 65 лет', callback_data='GoodAge')
        keyboard.add(key_age2)
        key_age3 = types.InlineKeyboardButton(text='Старше 65 лет', callback_data='BadAge')
        keyboard.add(key_age3)
        bot.send_message(call.message.chat.id, text='Укажите, пожалуйста, ваш возраст:\n', reply_markup=keyboard)

    if call.data == "GoodAge":
        keyboard = types.InlineKeyboardMarkup()
        key_age1 = types.InlineKeyboardButton(text='Россия / Беларусь', callback_data='GoodFinal')
        keyboard.add(key_age1)
        key_age2 = types.InlineKeyboardButton(text='Армения / Казахстан / Киргизия / Украина', callback_data='BadFinal')
        keyboard.add(key_age2)
        key_age3 = types.InlineKeyboardButton(text='Другое', callback_data='BadFinal')
        keyboard.add(key_age3)
        bot.send_message(call.message.chat.id, text='Укажите, пожалуйста, ваше гражданство:\n', reply_markup=keyboard)

    if call.data == "BadAge":
        keyboard = types.InlineKeyboardMarkup()
        key_age1 = types.InlineKeyboardButton(text='Россия / Беларусь', callback_data='BadFinal')
        keyboard.add(key_age1)
        key_age2 = types.InlineKeyboardButton(text='Армения / Казахстан / Киргизия / Украина',
                                              callback_data='BadFinal')
        keyboard.add(key_age2)
        key_age3 = types.InlineKeyboardButton(text='Другое', callback_data='BadFinal')
        keyboard.add(key_age3)
        bot.send_message(call.message.chat.id, text='Укажите, пожалуйста, ваше гражданство:\n', reply_markup=keyboard)

    if call.data == "BadFinal":
        bot.send_message(call.message.chat.id, text="Спасибо за предоставленную информацию!\nМы передадим ваши данные на рассмотрение специалистам.\nВ случае положительного решения мы с вами свяжемся в течение двух рабочих дней.\n")

    if call.data == "GoodFinal":
        photo2 = open('test_teremok_route.jpeg', 'rb')
        photo3 = open('test_teremok_entrance.jpeg', 'rb')
        bot.send_message(call.message.chat.id, text="Отлично!\nПриходите на собеседование в будни с 09:00 до 17:00.\nм. Парк Культуры, ул. Зубовский бульвар дом 22/39 (7 мин., пешком).\nДеловой Центр \'Пречистенка\' (два льва у входа). Из стеклянных дверей направо, второй лифт, на лифте на 5 этаж.\nПо возможности возьмите с собой паспорт, ИНН, СНИЛС, трудовую книжку, если есть - документ об образовании и медицинскую книжку.\nТелефон для связи +7 495 736 96 95 или 8 800 333 31 20 (звонок бесплатный!)",photo=[photo2, photo3])

    if call.data == "Refuse2":

    if call.data == "Refuse1":
        bot.send_message(call.message.chat.id, text="Пожалуйста, подскажите, почему Вам не интересна эта вакансия?")
        keyboard = types.InlineKeyboardMarkup()
        key_decl1 = types.InlineKeyboardButton(text='Мне не подходит должность', callback_data='Decline1')
        keyboard.add(key_decl1)
        key_decl2 = types.InlineKeyboardButton(text='Не хочу работать в общепите', callback_data='Decline2')
        keyboard.add(key_decl2)
        key_decl3 = types.InlineKeyboardButton(text='Не подходит город', callback_data='Decline3')
        keyboard.add(key_decl3)
        key_decl4 = types.InlineKeyboardButton(text='Ищу работу не для себя', callback_data='Decline4')
        keyboard.add(key_decl4)
        key_decl5 = types.InlineKeyboardButton(text='Другая причина', callback_data='Decline5')
        keyboard.add(key_decl5)
