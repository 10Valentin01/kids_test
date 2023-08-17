from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup


def keyboards_btn():
    kb = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    btn_list = ['Фото из школы', 'Мое хобби', 'Мое последнее фото из телефона']
    for i in btn_list:
        kb.add(KeyboardButton(i))
    return kb


def inline_keyboard_btn():
    kb = InlineKeyboardMarkup(row_width=1)
    btn_list = ['Отличия SQL от NoSql', 'Что такое ChatGPT?', 'История первой любви']
    for i in btn_list:
        kb.add(InlineKeyboardButton(text=i, callback_data=i))

    return kb