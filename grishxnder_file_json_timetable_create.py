"""
grishxnder file of project.

this file will be doing something.

"""
import json


class TimeTable:
    def __init__(self, time_table_file_name):
        self.time_table_file_name = time_table_file_name
        try:
            start_date = 16
            json_dict_main = dict()
            day_routine = []
            with open(time_table_file_name, 'r', encoding='utf-8') as time_table:
                for line in time_table:
                    dict_for_the_day = dict()
                    if not(line.split()):
                        start_date += 1
                        day_routine = []
                    else:
                        activity = ''
                        time = ''
                        for word_index in range(3):
                            time += line.split()[word_index]
                        for word_index in range(3, len(line.split())):
                            if word_index != 3:
                                activity += ' '
                            activity += line.split()[word_index]
                        dict_for_the_day[time] = activity
                        day_routine.append(dict_for_the_day)

                    json_dict_main[start_date] = day_routine
                json_dic_main_main = dict()
                json_dic_main_main['1'] = json_dict_main
                json_dic_main_main['2'] = json_dict_main
                json_dic_main_main['3'] = json_dict_main
                json_dic_main_main['4'] = json_dict_main
                json_dic_main_main['5'] = json_dict_main
            with open("json_timetable.json", "w", encoding="utf-8") as file:
                json.dump(json_dic_main_main, file, indent=4, ensure_ascii=False,  separators=(',', ': '))
            time_table.close()
        except IOError:
            print("Ошибка открытия файла IOError!")


t = TimeTable('time_table.txt')







