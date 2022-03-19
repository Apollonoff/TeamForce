from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = ''

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

bot_father_id = 93372553


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


@dp.message_handler(commands=['create'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Input topic!")


@dp.message_handler()
async def echo(message: types.Message):
    mes = message.text
    print(mes)


executor.start_polling(dp, skip_updates=True)

