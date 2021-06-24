import logging
from aiogram import Bot, Dispatcher, executor, types
import config
from datetime import date, datetime
from time_worker import Shedule
import json
from jsonreader import set_squad, get_squad

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
buttons_function = ["Мероприятия сейчас", "Следующее мероприятие",
                    "Расписание на сегодня", "Контакты",
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
contacts = {
    "Организаторы": "Почта - mail@innopoliscamp.ru \nКонтактный номер - 8-965-583-19-27 \nАдрес - г. Иннополис, ул. Квантовый бульвар, д.1, здание Лицея Иннополис.",
    "Администрация": "Руководитель смены Эльшад Бахшиев @elshadbah\n Старший вожатый Татьяна Онищенко @o_teta_a\nПедагог-организатор Диана Куличенко @kulichik_di\nСтарший преподаватель Анастасия Андронова +7 999 232-15-71 @andronova_anastasia \nМедицинский работник Наиля Набиева 89869233503 @Nabi0987\nАдминистратор смены Рустам Хамидуллин +7 951 065-12-48 @Rstm_Khan\nСпортинструктор Дарья Капитурова +7 987 457-16-07 @raven_rch\nЗвукооператор Виталий Сапожников +7 904 767-48-52 @Hawk_Prime",
    "Преподаватели": "У InnoCamp 11 преподавателей по направлениям: \n [Minecraft] Камилла Хамидуллина - @Kamila_ak \n [App Inventor] Макше Сейткалиев - @seytkalievm \n [Scratch] Маргарита Сидорская - @RitaSidorskya \n [Python] Никита Носков - @MPardis \n [C#] Артем Сахаров - @ilostmygoddamnson \n [Java] Артемий Кочергин - @treatn \n [Дизайн] Динар Шамсутдинов - @d_shamik \n [Маркетинг] Марина Лебединская - @mari1861 \n [Управление] Анастасия Андронова - @andronova_anastasia \n [Продвинутый Python] Макар Шевченко - @SyrexMinus \n [Проектная мастерская] Евгений Сазонов - @EvgenySazonov",
    "Вожатые": "1 отряд:\n Владимир Прокопенко(@prokov) и Юлия Кузьмина(@kyzminajulia) \n\n2 отряд:\n Алина Турчина(@lunallina) и Константин Воробьев \n\n3 отряд:\n Ксения Панасова(@KseniaHope20) и Мохамед Агатанов(@Demahom)  \n\n4 отряд:\n Дамир Нуртдинов(@Damurka5) Екатерина Мацнева(@matsnevakat)  \n\n5 отряд:\n Иван Булатов (@cffeeman) и Алиса Тимофеева (@Alisainno18) ",
    "Остальные": "DJ(диджей) - Виталий - +79047674852, \n Педагог-организатор @kulichik_di"
}


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
        least_time = str(function_schedule.remaining_time())
        quan_minutes = least_time.split(":")[1]
        quan_hours = least_time.split(":")[0]
        quan_seconds = least_time.split(':')[2]
        if name_activity:
            await message.answer(
                f"—————————————————— \n"
                f"🔻➡️ У отряда №{author_group} сейчас {name_activity[1]} \n"
                f"⏰ Продолжительность {name_activity[0]}(осталось {quan_hours}:{quan_minutes}:{quan_seconds}) \n"
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
        for i in timetable.keys():
            result += f"⭕ {i} {timetable[i]}\n"
        result += "——————————————————"
        await message.answer(result,
                             reply_markup=keyboard_function)
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


@dp.message_handler(lambda message: message.text == "Следующее мероприятие")
async def further_now(message: types.Message):
    time_now = datetime.now()
    author_id = str(message.from_user.id)
    author_group = get_squad(author_id)
    if author_group:
        function_schedule = Shedule(time_now, author_group)
        name_activity = function_schedule.what_next()
        least_time = str(function_schedule.remaining_to_next())
        quan_minutes = least_time.split(":")[1]
        quan_hours = least_time.split(":")[0]
        quan_seconds = least_time.split(":")[2]
        await message.answer(
            f"—————————————————— \n"
            f"🔻➡️ У отряда №{author_group} следующее мероприятие: {name_activity[1]} \n \n"
            f"⏰ Продолжительность {name_activity[0]}(осталось {quan_hours}:{quan_minutes}:{quan_seconds}) \n"
            f"——————————————————")
    else:
        await message.answer(f"🛑 Вы не выбрали отряд! 🛑",
                             reply_markup=keyboard_start)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
