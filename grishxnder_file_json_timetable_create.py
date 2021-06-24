"""
grishxnder file of project.

this file will be doing something.

"""
from openpyxl import load_workbook
import json
from datetime import date as date1


class TimeTable:
    def __init__(self, time_table_file_name, ):
        self.time_table_file_name = time_table_file_name  # установили time_table_file_name в атрибут имя файла
        if time_table_file_name.split('.')[1] == 'txt':
            try:

                json_dict_main = dict() # создание словаря для заполнения одного отряда
                json_dic_main_main = dict()  # итоговый словарь
                with open(time_table_file_name, 'r', encoding='utf-8') as time_table:
                    date = int(time_table.readline().split()[0])  # Начало смены
                    dict_for_the_day = dict()  # словарь для заполнения дня
                    for line in time_table:  # начинем читать файл построчно
                        if (len(line.split()) <= 2) and (len(line.split()) > 0):  # если попалась пустая линия(означает следующий день)
                            json_dict_main[date] = dict_for_the_day  # в словарь расписания отряда записываем словварь дня
                            dict_for_the_day = dict()  # обновляем словарь дня
                            date = int(line.split()[0])  # увеличиваем дату
                        else:
                            time = ''  # переменная для хранения времени
                            activity = ''  # переменная для хранения занятия

                            # Цикл для добавления времени в нужный формат time = line.split()[:3] - эквивалентно
                            for word_index in range(3):
                                time += line.split()[word_index]

                            # Цикл для добавления активности
                            for word_index in range(3, len(line.split())):
                                if word_index != 3:
                                    activity += ' '
                                activity += line.split()[word_index]

                            dict_for_the_day[time] = activity  # Добавляем в словарь дня время и занятие в это время

                    # Добавление расписания для отрядов: 1, 2, 3, 4, 5
                    json_dic_main_main['1'] = json_dict_main
                    json_dic_main_main['2'] = json_dict_main
                    json_dic_main_main['3'] = json_dict_main
                    json_dic_main_main['4'] = json_dict_main
                    json_dic_main_main['5'] = json_dict_main

                # открываем файл json_timetable.json для записи json_dic_main_main(итога)
                with open("json_timetable.json", "w", encoding="utf-8") as file:
                    # Запись в json-file словаря
                    json.dump(json_dic_main_main, file, indent=4, ensure_ascii=False,  separators=(',', ': '))

                time_table.close()  # Закрываем текстовый файл.
            except IOError:
                print("Ошибка открытия файла IOError!")
        elif time_table_file_name.split('.')[1] == 'xlsx':
            work_book = load_workbook(filename=self.time_table_file_name)
            sheet = work_book['Лист1']
            not_empty = True
            line = 1
            date = str(sheet[f'A{line}'].value).split()[0]
            json_dict_main = dict()  # создание словаря для заполнения одного отряда
            json_dic_main_main = dict()  # итоговый словарь
            dict_for_the_day = dict()
            blank_lines = 0
            while not_empty:
                if len(str(sheet[f'A{line}'].value).split()) == 2:
                    json_dict_main[date] = dict_for_the_day  # в словарь расписания отряда записываем словварь дня
                    dict_for_the_day = dict()  # обновляем словарь дня
                    date = str(sheet[f'A{line}'].value).split()[0]  # увеличиваем дату
                    line += 1
                elif sheet[f'A{line}'].value is None:
                    blank_lines += 1
                    if blank_lines == 2:
                        not_empty = False
                else:
                    time_start = str(sheet[f'A{line}'].value)[:2]
                    time_finish = str(sheet[f'B{line}'].value)[:2]
                    time = f'{time_start}-{time_finish}'
                    activity = sheet[f'C{line}'].value
                    dict_for_the_day[time] = activity
                    blank_lines = 0
                    line += 1

            json_dic_main_main['1'] = json_dict_main
            json_dic_main_main['2'] = json_dict_main
            json_dic_main_main['3'] = json_dict_main
            json_dic_main_main['4'] = json_dict_main
            json_dic_main_main['5'] = json_dict_main
            with open("json_timetable_excel.json", "w", encoding="utf-8") as file:
                # Запись в json-file словаря
                json.dump(json_dic_main_main, file, indent=4, ensure_ascii=False, separators=(',', ': '))








