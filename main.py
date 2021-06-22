import logging
from aiogram import Bot, Dispatcher, executor, types
import config
from datetime import date

# Объект бота
bot = Bot(token=config.TOKEN)
# Диспетчер для бота
dp = Dispatcher(bot)
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

keyboard_general = types.ReplyKeyboardMarkup(resize_keyboard=False)
keyboard_group = types.ReplyKeyboardMarkup(resize_keyboard=False)
keyboard_function = types.ReplyKeyboardMarkup(resize_keyboard=False)
buttons_function = ["Мероприятия сейчас", "Расписание на сегодня", "Контакты",
                    "Главное меню"]
buttons_general = ["Выбрать отряд", "Общая информация", "Контакты"]
buttons_group = ["5 отряд", "4 отряд", "3 отряд", "2 отряд", "1 отряд"]
keyboard_general.add(*buttons_general)
keyboard_group.add(*buttons_group)
keyboard_function.add(*buttons_function)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.answer("Привет!", reply_markup=keyboard_general)


@dp.message_handler(commands="test1")
async def cmd_test1(message: types.Message):
    await message.reply("Test 1")


@dp.message_handler(lambda message: message.text == "Выбрать отряд")
async def choose_group(message: types.Message):
    await message.answer("Выбери отряд с 1 по 5 номер",
                         reply_markup=keyboard_group)


@dp.message_handler(
    lambda message: message.text in ["1 отряд", "2 отряд", "3 отряд",
                                     "4 отряд", "5 отряд"])
async def registration(message: types.Message):
    await message.answer(
        f"{message.chat.id}, Ваш отряд номер {message.text.split()[0]}",
        reply_markup=keyboard_function)


@dp.message_handler(lambda message: message.text == "Мероприятия сейчас")
async def choose_group(message: types.Message):
    await message.answer("Ошибка загрузки")


@dp.message_handler(lambda message: message.text == "Расписание на сегодня")
async def choose_group(message: types.Message):
    today_time = (date.today().day, date.today().month)
    await message.answer(f"Сегодня {today_time[0]}.{today_time[1]}",
                         reply_markup=keyboard_function)


@dp.message_handler(lambda message: message.text == "Главное меню")
async def choose_group(message: types.Message):
    await message.answer("Вы перешли в главное меню",
                         reply_markup=keyboard_general)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
