import telebot
from telebot import types
from decouple import config


TOKEN = config('TOKEN')
bot = telebot.TeleBot(TOKEN)

user_states = {}


@bot.message_handler(commands=['start'])
def start(message):

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton('🇺🇿 O\'zbekcha'))
    keyboard.add(types.KeyboardButton('🇷🇺 Русский'))
    keyboard.add(types.KeyboardButton('🇬🇧 English'))

    bot.send_message(message.chat.id, """
    Здравствуйте! Давайте для начала выберем язык обслуживания.
                    
Keling, avvaliga xizmat ko’rsatish tilini tanlab olaylik.
                    
Hi! Let's first choose the language of serving.
    """, reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text in ['🇺🇿 O\'zbekcha', '🇷🇺 Русский', '🇬🇧 English'])
def language_selected(message):


    if message.text == '🇺🇿 O\'zbekcha' or  message.text == '⬅️ Ortga':

        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(types.KeyboardButton('🍽 Menyu'))
        keyboard.add(types.KeyboardButton('📖 Buyurtmalar tarixi'), types.KeyboardButton('✍️ Fikr bildirish'))
        keyboard.add(types.KeyboardButton('ℹ️ Ma\'lumot'), types.KeyboardButton('☎️ Biz bilan aloqa'))
        keyboard.add(types.KeyboardButton('⚙️ Sozlamalar'))

        bot.send_message(message.chat.id, "Bosh menyu", reply_markup=keyboard)

    elif message.text == '🇬🇧 English' or  message.text == '⬅️ Back':

        keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        keyboard.add(types.KeyboardButton('🍽 Menu'))
        keyboard.add(types.KeyboardButton('📖 Order History'), types.KeyboardButton('✍️ Give Feedback'))
        keyboard.add(types.KeyboardButton('ℹ️ Information'), types.KeyboardButton('☎️ Contact Us'))
        keyboard.add(types.KeyboardButton('⚙️ Settings'))

        bot.send_message(message.chat.id, "Main menu", reply_markup=keyboard)
    
    elif message.text == '🇷🇺 Русский' or message.text == '⬅️ Назад':  

        keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        keyboard.add(types.KeyboardButton('🍽 Меню'))
        keyboard.add(types.KeyboardButton('📖 История заказов'), types.KeyboardButton('✍️ Оставить отзыв'))
        keyboard.add(types.KeyboardButton('ℹ️ Информация'), types.KeyboardButton('☎️ Контакты'))
        keyboard.add(types.KeyboardButton('⚙️ Настройки'))

        bot.send_message(message.chat.id, "Главное меню", reply_markup=keyboard)

   
@bot.message_handler(func=lambda message: message.text in ['⚙️ Sozlamalar', '⚙️ Settings', '⚙️ Настройки'])
def settings(message):

    if message.text == '⚙️ Sozlamalar':
        user_states[message.chat.id] = "sozlamalar"  

        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(types.KeyboardButton('Ismni o’zgartirish'), types.KeyboardButton('📱 Raqamni o’zgartirish'))
        keyboard.add(types.KeyboardButton('🏙 Shaharni o\'zgartirish'), types.KeyboardButton('🇺🇿 Tilni o\'zgartirish'))
        keyboard.add(types.KeyboardButton('⬅️ Ortga'))

        bot.send_message(message.chat.id, "Tanlang:", reply_markup=keyboard)

    elif message.text == '⚙️ Settings':
        user_states[message.chat.id] = "settings"  
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        keyboard.add(types.KeyboardButton('Change name'), types.KeyboardButton('📱 Change number'))
        keyboard.add(types.KeyboardButton('🏙 Change city'), types.KeyboardButton('🇬🇧 Change Language'))
        keyboard.add(types.KeyboardButton('⬅️ Back'))

        bot.send_message(message.chat.id, "Choose", reply_markup=keyboard)

    elif message.text == '⚙️ Настройки':
        user_states[message.chat.id] = "настройки"  

        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        keyboard.add(types.KeyboardButton('Изменить имя'), types.KeyboardButton('📱 Изменить номер'))
        keyboard.add(types.KeyboardButton('🏙 Изменить город'), types.KeyboardButton('🇷🇺 Изменить язык'))
        keyboard.add(types.KeyboardButton('⬅️ Назад'))

        bot.send_message(message.chat.id, "Выбирать", reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text in ['🍽 Меню', '🍽 Menu', '🍽 Menyu'])
def settings(message):

    if message.text == '🍽 Menyu':
        user_states[message.chat.id] = "menu"  

        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(types.KeyboardButton('🚙 Yetkazib berish'), types.KeyboardButton('🏃 Olib ketish'))
        keyboard.add(types.KeyboardButton('⬅️ Ortga'))

        bot.send_message(message.chat.id, "Tanlang:", reply_markup=keyboard)

    elif message.text == '🍽 Menu':
        user_states[message.chat.id] = "menu"  
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        keyboard.add(types.KeyboardButton('🚙 Delivery'), types.KeyboardButton('🏃 Pickup'))

        keyboard.add(types.KeyboardButton('⬅️ Back'))

        bot.send_message(message.chat.id, "Choose", reply_markup=keyboard)

    elif message.text == '🍽 Меню':
        user_states[message.chat.id] = "menu"  

        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        keyboard.add(types.KeyboardButton('🚙 Доставка'), types.KeyboardButton('🏃 Самовывоз'))
        keyboard.add(types.KeyboardButton('⬅️ Назад'))

        bot.send_me

@bot.message_handler(func=lambda message: message.text in ['⬅️ Back', '⬅️ Ortga', '⬅️ Назад'])
def back_to_previous(message):
    if message.chat.id in user_states:
        if user_states[message.chat.id] == "settings":
            language_selected(message)  
        elif user_states[message.chat.id] == "sozlamalar":
            language_selected(message)  
        elif user_states[message.chat.id] == "настройки":
            language_selected(message)
        elif user_states[message.chat.id] == "menu":
            language_selected(message)
        
    else:
        start(message)  


bot.polling()
