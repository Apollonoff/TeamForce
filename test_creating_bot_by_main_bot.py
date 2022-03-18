from aiogram import Bot, Dispatcher, executor, types
from time import sleep

API_TOKEN = '1173555697:AAEaopgYWpRjDn9WBuXHup5hwtCp5Dz6ehI'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

bot_father_id = 93372553


@dp.message_handler(commands=['start', 'help', 'create'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Input topic!")


@dp.message_handler()
async def echo(message: types.Message):
    mes = message.text
    print(mes)
#    await message.answer(message.text)


# async def send_message_to_bot_father():
#
#     await bot.send_message(bot_father_id, '/newbot')
#     sleep(3)
#     await bot.send_message(bot_father_id, 'urod_and_beauty')


executor.start_polling(dp, skip_updates=True)



