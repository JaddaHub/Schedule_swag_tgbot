TOKEN = "1764663180:AAEDQ0PUshlrY-e_EhIwTlvaMqwHngQrzb8"
json_path = 'users_data.json'
contacts_json_path = 'json_contacts.json'
audio_ogg_to_wav = "audio.ogg"
audio_to_recognise = "audio.wav"
json_name = 'json_timetable.json'

voice_commands = {

    # при добалении голосовой функции ставь в конце "_",

    'change_group_': {'изменить', 'отряд'},
    'registration_': {'первый', 'второй', 'третий', 'четвертый', 'пятый',
                      'отряд'},
    'event_now_': {'мероприятия', 'сейчас'},
    'timetable_today_': {'расписание', 'на', 'сегодня'},
    'timetable_tomorrow_': {'расписание', 'на', 'завтра'},
    'general_info_': {'общая', 'информация'},
    'contact_menu_': {'контакты'},
    'Администрация': {'администрация'},
    'Организаторы': {'рганизаторы'},
    'Преподаватели': {'преподаватели'},
    'Вожатые': {'вожатые'},
    'Остальные': {'остальные'}
}
