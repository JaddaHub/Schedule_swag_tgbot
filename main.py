import logging
from aiogram import Bot, Dispatcher, executor, types
import config
from datetime import date, datetime
from time_worker import Shedule
from jsonreader import set_squad, get_squad, get_contacts
import speech_recognition as sr
import subprocess
from voice_worker import del_audio_files, CommandSelector

r = sr.Recognizer()

# Объект бота
bot = Bot(token=config.TOKEN)
# Диспетчер для бота
dp = Dispatcher(bot)
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

keyboard_general = types.ReplyKeyboardMarkup(resize_keyboard=False)
keyboard_group = types.ReplyKeyboardMarkup(resize_keyboard=False)
keyboard_function = types.ReplyKeyboardMarkup(resize_keyboard=False)
keyboard_start = types.ReplyKeyboardMarkup(resize_keyboard=False)
keyboard_contacts = types.ReplyKeyboardMarkup(resize_keyboard=False)
buttons_function = ["Мероприятия сейчас", "Расписание на сегодня",
                    "Расписание на завтра", "Контакты",
                    "Общая информация", "Изменить отряд"]
buttons_contacts = ["Организаторы", "Администрация", "Преподаватели",
                    "Вожатые", "Остальные"]
buttons_start = ["Выбрать отряд"]
buttons_group = ["5 отряд", "4 отряд", "3 отряд", "2 отряд", "1 отряд"]
keyboard_general.add(*buttons_start)
keyboard_group.add(*buttons_group)
keyboard_start.add(*buttons_start)
keyboard_function.add(*buttons_function)
keyboard_contacts.add(*buttons_contacts)
contacts = get_contacts()


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.answer(
        "👋 Привет! Этот бот был специально разработан для Лицея Иннополиса. Он умеет выдавать расписание 📚 на текущий день, мероприятие в данный момент 📜 \n \n"
        "𝔭𝔯𝔬𝔡. 𝔟𝔶 𝔅𝔘𝔉𝔉𝔐ℑ",
        reply_markup=keyboard_start)


@dp.message_handler(lambda message: message.text == "Выбрать отряд")
async def choose_group(message: types.Message):
    await message.answer("Выберите отряд с 1 по 5 номер 👇",
                         reply_markup=keyboard_group)


@dp.message_handler(lambda message: message.text == "Изменить отряд")
async def change_group(message: types.Message):
    await message.answer("Выберите отряд с 1 по 5 номер 👇",
                         reply_markup=keyboard_group)


@dp.message_handler(
    lambda message: message.text in ["1 отряд", "2 отряд", "3 отряд",
                                     "4 отряд", "5 отряд"])
async def registration(message: types.Message):
    author_id = str(message.from_user.id)
    otryad_number = message.text.split()[0]
    set_squad(author_id, otryad_number)
    await message.answer(
        f"✅ Вы выбрали отряд номер {message.text.split()[0]}",
        reply_markup=keyboard_function)


@dp.message_handler(lambda message: message.text == "Мероприятия сейчас")
async def event_now(message: types.Message):
    time_now = datetime.now()
    author_id = str(message.from_user.id)
    author_group = get_squad(author_id)
    if author_group:
        function_schedule = Shedule(time_now, author_group)
        name_activity = function_schedule.what_now()
        if name_activity is not None:
            least_time = str(function_schedule.remaining_time())
            quan_minutes = least_time.split(":")[1]
            quan_hours = least_time.split(":")[0]
            quan_seconds = least_time.split(':')[2]
            name_activity_next = function_schedule.what_next()
            least_time_next = str(function_schedule.remaining_to_next())
            quan_minutes_next = least_time_next.split(":")[1]
            quan_hours_next = least_time_next.split(":")[0]
            quan_seconds_next = least_time_next.split(":")[2]
            if name_activity:
                await message.answer(
                    f"—————————————————— \n"
                    f"🔻➡️ У отряда №{author_group} сейчас {name_activity[1]} \n"
                    f"⏰ Продолжительность {name_activity[0]}(осталось {quan_hours}:{quan_minutes}:{quan_seconds}) \n \n"
                    f"➡ Следующее мероприятие {name_activity_next[1]}\n⏰ Продолжительность {name_activity_next[0]}(до него осталось {quan_hours_next}:{quan_minutes_next}:{quan_seconds_next}) \n"
                    f"——————————————————")
            else:
                await message.answer(
                    f"—————————————————— \n"
                    f"🔻➡️ У отряда №{author_group} сейчас свободное время \n"
                    f"——————————————————")
        else:
            await message.answer(
                f"—————————————————— \n"
                f"🔻➡️ У отряда №{author_group} сейчас свободное время \n"
                f"——————————————————")
    else:
        await message.answer(f"🛑 Вы не выбрали отряд! 🛑",
                             reply_markup=keyboard_start)


@dp.message_handler(lambda message: message.text == "Расписание на сегодня")
async def timetable_today(message: types.Message):
    time_now = datetime.now()
    author_id = str(message.from_user.id)
    author_group = get_squad(author_id)
    if author_group:
        result = "—————————————————— \n"
        result += f"🟥 Расписание {author_group} отряда \n"
        result += "—————————————————— \n"
        function_table = Shedule(time_now, author_group)
        timetable = function_table.show_shedule()
        if timetable is not None:
            for i in timetable.keys():
                result += f"⭕ {i} {timetable[i]}\n"
            result += "——————————————————"
            await message.answer(result,
                                 reply_markup=keyboard_function)
        else:
            await message.answer(f"🛑 Расписания на сегодня нет 🛑",
                                 reply_markup=keyboard_start)
    else:
        await message.answer(f"🛑 Вы не выбрали отряд! 🛑",
                             reply_markup=keyboard_start)


@dp.message_handler(lambda message: message.text == "Расписание на завтра")
async def timetable_tomorrow(message: types.Message):
    time_now = datetime.now()
    author_id = str(message.from_user.id)
    author_group = get_squad(author_id)
    if author_group:
        result = "—————————————————— \n"
        result += f"🟥 Расписание {author_group} отряда на завтра \n"
        result += "—————————————————— \n"
        function_table = Shedule(time_now, author_group)
        timetable = function_table.show_shedule_tomorrow()
        if timetable is not None:
            for i in timetable.keys():
                result += f"⭕ {i} {timetable[i]}\n"
            result += "——————————————————"
            await message.answer(result,
                                 reply_markup=keyboard_function)
        else:
            await message.answer(f"🛑 Расписания на завтра нет 🛑",
                                 reply_markup=keyboard_start)
    else:
        await message.answer(f"🛑 Вы не выбрали отряд! 🛑",
                             reply_markup=keyboard_start)


@dp.message_handler(lambda message: message.text == "Общая информация")
async def general_info(message: types.Message):
    await message.answer(
        "🏖️ Детские IT-каникулы с заботой о ребёнке в Иннополисе. "
        "Ваш ребенок научится создавать:\n ➡ мобильные приложения"
        "\n ➡ компьютерные игры \n ➡ чат-ботов"
        "\n ➡ проектировать дизайн интерфейсов"
        "\n ➡ продвигать IT-продукты в интернете и управлять IT-командой!",
        reply_markup=keyboard_function)


@dp.message_handler(lambda message: message.text == "Контакты")
async def contact_menu(message: types.Message):
    result = "Выберите группу людей которая вас интересует"
    await message.answer(result,
                         reply_markup=keyboard_contacts)


@dp.message_handler(lambda message: message.text in buttons_contacts)
async def contact_menu(message: types.Message):
    result = f"{message.text}:\n {contacts[message.text]} \n \n "
    await message.answer(result,
                         reply_markup=keyboard_function)


@dp.message_handler(state="*", content_types="voice")
async def get_voice(message: types.Message):
    file_ID = message.voice.file_id
    file = await bot.get_file(file_ID)
    file_path = file.file_path
    await bot.download_file(file_path, "audio.ogg")
    src_filename = 'audio.ogg'
    dest_filename = 'audio.wav'
    process = subprocess.run(['ffmpeg', '-i', src_filename, dest_filename])
    if process.returncode != 0:
        raise Exception("Something went wrong")
    file = sr.AudioFile('audio.wav')
    with file as source:
        audio = r.record(source)
        text = r.recognize_google(audio, language="ru_RU")
        await message.answer(f"Ваш текст: {text}")

    del_audio_files()

    cs = CommandSelector(text)
    exec(f'{cs.get_recognized_function()}({message})')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
