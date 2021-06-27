from pymorphy2 import MorphAnalyzer
import os
from config import audio_ogg_to_wav, audio_to_recognise, voice_commands, \
    words2num

path_ogg_file = audio_ogg_to_wav
path_wav_file = audio_to_recognise


def del_audio_files():
    try:
        os.remove(path_ogg_file)
        os.remove(path_wav_file)
    except FileNotFoundError:
        return


class CommandSelector:
    def __init__(self, text):
        self.morph = MorphAnalyzer()
        self.validate_value_to_normal(voice_commands)
        self.words2num = self.validate_keys_to_normal(words2num)
        self.spoken_word = set()
        self.matches = dict([(key, 0) for key in voice_commands])

        for word in text.split():
            self.spoken_word.add(self.morph.normal_forms(word)[0])

        for command in voice_commands:
            self.matches[command] = len(
                self.spoken_word & voice_commands[command])
        self.command = max(self.matches.items(), key=lambda x: x[1])[0]
        if self.command == 'registration_':
            for word in words2num:
                if word in self.spoken_word:
                    self.command += words2num[word]
                    break

    def get_recognized_function(self):
        return self.command

    def validate_value_to_normal(self, voice_commands):
        for command, value in voice_commands.items():
            res_words = set()
            for word in value:
                res_words.add(self.morph.normal_forms(word)[0])
            voice_commands[command] = res_words

    def validate_keys_to_normal(self, dict_):
        new_dict = dict()
        for key, value in dict_.items():
            new_dict[self.morph.normal_forms(key)[0]] = value
        return new_dict


if __name__ == '__main__':
    cs = CommandSelector('поставь первое отряд')
    print(cs.get_recognized_function())
