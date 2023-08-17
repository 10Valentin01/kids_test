import asyncio

from aiogram.types.base import InputFile

from create import dp, bot
from .messages_from_V import *
from .functions import *


from aiogram import types
from aiogram.dispatcher.filters import Text
from aiogram.types import Message, CallbackQuery


@dp.message_handler(commands='start')
async def start_message(message: Message):
    await message.answer(start_message_V, parse_mode='HTML', reply_markup=keyboards_btn())
    await asyncio.sleep(2)
    await message.answer('Также дополнительный команды вы можете увидеть, нажав на кнопку <b>"Меню"</b>',
                         parse_mode='HTML')


@dp.message_handler(Text(equals='Фото из школы'))
async def send_school_photo(message: Message):
    photo = open('commands_user/photo/school.jpg', 'rb')
    await message.answer_photo(photo=photo, caption=about_school_photo, reply_markup=keyboards_btn())


@dp.message_handler(Text(equals='Мое последнее фото из телефона'))
async def send_school_photo(message: Message):
    photo = open('commands_user/photo/wending.jpg', 'rb')
    await message.answer_photo(photo=photo, caption=about_last_photo, parse_mode='HTML', reply_markup=keyboards_btn())


@dp.message_handler(Text(equals='Мое хобби'))
async def send_school_photo(message: Message):
    photo = open('commands_user/photo/hobby.jpg', 'rb')
    await message.answer_photo(photo=photo, caption=about_hobby, parse_mode='HTML', reply_markup=keyboards_btn())


@dp.message_handler(Text(equals='Git'))
async def send_school_photo(message: Message):
    await message.answer('https://github.com/10Valentin01/kids_test')


@dp.message_handler(commands='voice')
async def menu_voice_message(message: Message):
    await message.answer(voice_message, reply_markup=inline_keyboard_btn())


@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith("Отличия"))
async def sql_callback(callback: CallbackQuery):
    voice = open('commands_user/audio/SQL.ogg', 'rb')
    await bot.send_voice(chat_id=callback.from_user.id, voice=voice)
    await callback.answer()


@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith("Что"))
async def gpt_callback(callback: CallbackQuery):
    voice = open('commands_user/audio/GPT.ogg', 'rb')
    await bot.send_voice(chat_id=callback.from_user.id, voice=voice)
    await callback.answer()


@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith("История"))
async def love_callback(callback: CallbackQuery):
    voice = open('commands_user/audio/Love_story.ogg', 'rb')
    await bot.send_voice(chat_id=callback.from_user.id, voice=voice)
    await callback.answer()



