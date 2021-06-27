from pymorphy2 import MorphAnalyzer
import os

path_ogg_file = 'audio.ogg'
path_wav_file = 'audio.wav'

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


def del_audio_files():
    try:
        os.remove(path_ogg_file)
        os.remove(path_wav_file)
    except FileNotFoundError:
        return


class CommandSelector:
    def __init__(self, text):
        self.morph = MorphAnalyzer()
        self.__validating_voice_commands()
        self.spoken_word = set()
        self.matches = dict([(key, 0) for key in voice_commands])

        for word in text.split():
            self.spoken_word.add(self.morph.normal_forms(word)[0])

        for command in voice_commands:
            self.matches[command] = len(
                self.spoken_word & voice_commands[command])
        self.command = max(self.matches.items(), key=lambda x: x[1])[0]

    def get_recognized_function(self):
        return self.command

    def __validating_voice_commands(self):
        for command, value in voice_commands.items():
            res_words = set()
            for word in value:
                res_words.add(self.morph.normal_forms(word)[0])
            voice_commands[command] = res_words


if __name__ == '__main__':
    cs = CommandSelector('покажи администрацию')
    print(cs.get_recognized_function())
