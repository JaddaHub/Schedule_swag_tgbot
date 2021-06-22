import logging
from aiogram import Bot, Dispatcher, executor, types
import config

# Объект бота
bot = Bot(token=config.TOKEN)
# Диспетчер для бота
dp = Dispatcher(bot)
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

keyboard_general = types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_group = types.ReplyKeyboardMarkup(resize_keyboard=True)
buttons_general = ["Выбрать отряд", "Общая информация"]
buttons_group = ["5", "4", "3", "2", "1"]
keyboard_general.add(*buttons_general)
keyboard_group.add(*buttons_group)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.answer("Привет!", reply_markup=keyboard_general)


@dp.message_handler(commands="test1")
async def cmd_test1(message: types.Message):
    await message.reply("Test 1")


@dp.message_handler(lambda message: message.text == "Выбрать отряд")
async def registration(message: types.Message):
    await message.answer("Выбери отряд с 1 по 5 номер",
                         reply_markup=keyboard_group)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
