import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.bot import api

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

bot =Bot(
    token='1173555697:AAEaopgYWpRjDn9WBuXHup5hwtCp5Dz6ehI',
)

dp = Dispatcher(bot=bot,)

@dp.message_handler(commands=['help'])
async def send_menu(message: types.Message):
    await message.reply(
        text="Создать бота /create",
        reply=False
    )
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply('Привет! Я - главный бот!')
    await send_menu(message=message)

@dp.message_handler()
async def echo(message: types.Message):
    if message.text != "/create":
         mes = message.text
         print(mes)

@dp.message_handler(commands='create')
async def create_new_bot(message: types.Message):
    await message.reply("Введите имя бота")
    await echo()


def main():
    executor.start_polling(
        dispatcher=dp
    )

if __name__ == "__main__":
    main()