from create import dp, bot

from aiogram import executor
from commands_user import user


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)