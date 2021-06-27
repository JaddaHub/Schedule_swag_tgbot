"""
grishxnder file of project.
this file will be doing something.

ЧТОБЫ ВЫЗВАТЬ МОЙ КОД ПИШИ 'экземпляр = TimeTable('имя файла(директория)')' ПРИМЕР - 
t1 = TimeTable('time_table.txt') # или, конечный файл - json_timetable.json
t2 = TimeTable('time_table.xlsx') # конечный файл - json_timetable.json
"""

from openpyxl import load_workbook
import json


def time_formatted_for_groups(time, n):
    amount_of_groups = 5

    time_start = time.split('-')[0]
    time_finish = time.split('-')[1]

    hour_start = int(time_start.split(':')[0])
    minute_start = int(time_start.split(':')[1])
    hour_finish = int(time_finish.split(':')[0])
    minute_finish = int(time_finish.split(':')[1])

    delta_time = (hour_finish * 60 + minute_finish) - (hour_start * 60 + minute_start)
    time_for_group = delta_time // amount_of_groups

    for_group_hour = time_for_group // 60
    for_group_minute = time_for_group - for_group_hour * 60
    answer = []
    if (hour_start < 10) and (minute_start >= 10):
        answer.append(f'0{hour_start}:{minute_start}')
    elif (hour_start < 10) and (minute_start < 10):
        answer.append(f'0{hour_start}:0{minute_start}')
    elif (hour_start >= 10) and (minute_start < 10):
        answer.append(f'{hour_start}:0{minute_start}')
    elif (hour_start >= 10) and (minute_start >= 10):
        answer.append(f'{hour_start}:{minute_start}')

    for i in range(5):
        hour_start += for_group_hour
        if (minute_start + for_group_minute) >= 60:
            hour_start += 1
            minute_start = ((minute_start + for_group_minute) % 60)
        else:
            minute_start += for_group_minute
        if (hour_start < 10) and (minute_start >= 10):
            answer.append(f'0{hour_start}:{minute_start}')
        elif (hour_start < 10) and (minute_start < 10):
            answer.append(f'0{hour_start}:0{minute_start}')
        elif (hour_start >= 10) and (minute_start < 10):
            answer.append(f'{hour_start}:0{minute_start}')
        elif (hour_start >= 10) and (minute_start >= 10):
            answer.append(f'{hour_start}:{minute_start}')
    answer.append(f'{hour_finish}:{minute_finish}')
    return f'{answer[5 - n]}-{answer[6 - n]}'


class TimeTable:
    def __init__(self, time_table_file_name, ):
        self.time_table_file_name = time_table_file_name  # установили time_table_file_name в атрибут имя файла
        if time_table_file_name.split('.')[1] == 'txt':
            try:

                json_dict_main_1 = dict()  # создание словаря для заполнения одного отряда
                json_dict_main_2 = dict()  # создание словаря для заполнения одного отряда
                json_dict_main_3 = dict()  # создание словаря для заполнения одного отряда
                json_dict_main_4 = dict()  # создание словаря для заполнения одного отряда
                json_dict_main_5 = dict()  # создание словаря для заполнения одного отряда
                json_dic_main_main = dict()  # итоговый словарь
                with open(time_table_file_name, 'r', encoding='utf-8') as time_table:
                    date = int(time_table.readline().split()[0])  # Начало смены
                    dict_for_the_day_1 = dict()  # обновляем словарь дня
                    dict_for_the_day_2 = dict()  # обновляем словарь дня
                    dict_for_the_day_3 = dict()  # обновляем словарь дня
                    dict_for_the_day_4 = dict()  # обновляем словарь дня
                    dict_for_the_day_5 = dict()  # обновляем словарь дня
                    for line in time_table:  # начинем читать файл построчно
                        if (len(line.split()) <= 2) and (
                                len(line.split()) > 0):  # если попалась линия (17 июля или 17)(означает следующий день)

                            json_dict_main_1[
                                date] = dict_for_the_day_1  # в словарь расписания отряда записываем словварь дня
                            json_dict_main_2[
                                date] = dict_for_the_day_2  # в словарь расписания отряда записываем словварь дня
                            json_dict_main_3[
                                date] = dict_for_the_day_3  # в словарь расписания отряда записываем словварь дня
                            json_dict_main_4[
                                date] = dict_for_the_day_4  # в словарь расписания отряда записываем словварь дня
                            json_dict_main_5[
                                date] = dict_for_the_day_5  # в словарь расписания отряда записываем словварь дня

                            dict_for_the_day_1 = dict()  # обновляем словарь дня
                            dict_for_the_day_2 = dict()  # обновляем словарь дня
                            dict_for_the_day_3 = dict()  # обновляем словарь дня
                            dict_for_the_day_4 = dict()  # обновляем словарь дня
                            dict_for_the_day_5 = dict()  # обновляем словарь дня
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

                            if activity.lower() == 'обед' or activity.lower() == 'ужин' or activity.lower() == 'завтрак' or activity.lower() == 'сонник' or activity.lower() == 'полдник':
                                dict_for_the_day_1[time_formatted_for_groups(time,
                                                                             1)] = activity  # Добавляем в словарь дня время и занятие в это время
                                dict_for_the_day_2[time_formatted_for_groups(time,
                                                                             2)] = activity  # Добавляем в словарь дня время и занятие в это время
                                dict_for_the_day_3[time_formatted_for_groups(time,
                                                                             3)] = activity  # Добавляем в словарь дня время и занятие в это время
                                dict_for_the_day_4[time_formatted_for_groups(time,
                                                                             4)] = activity  # Добавляем в словарь дня время и занятие в это время
                                dict_for_the_day_5[time_formatted_for_groups(time,
                                                                             5)] = activity  # Добавляем в словарь дня время и занятие в это время
                            else:
                                dict_for_the_day_1[
                                    time] = activity  # Добавляем в словарь дня время и занятие в это время
                                dict_for_the_day_2[
                                    time] = activity  # Добавляем в словарь дня время и занятие в это время
                                dict_for_the_day_3[
                                    time] = activity  # Добавляем в словарь дня время и занятие в это время
                                dict_for_the_day_4[
                                    time] = activity  # Добавляем в словарь дня время и занятие в это время
                                dict_for_the_day_5[
                                    time] = activity  # Добавляем в словарь дня время и занятие в это время

                            if date == 29:
                                json_dict_main_1[
                                    date] = dict_for_the_day_1  # в словарь расписания отряда записываем словварь дня
                                json_dict_main_2[
                                    date] = dict_for_the_day_2  # в словарь расписания отряда записываем словварь дня
                                json_dict_main_3[
                                    date] = dict_for_the_day_3  # в словарь расписания отряда записываем словварь дня
                                json_dict_main_4[
                                    date] = dict_for_the_day_4  # в словарь расписания отряда записываем словварь дня
                                json_dict_main_5[
                                    date] = dict_for_the_day_5  # в словарь расписания отряда записываем словварь дня

                    # Добавление расписания для отрядов: 1, 2, 3, 4, 5
                    json_dic_main_main['1'] = json_dict_main_1
                    json_dic_main_main['2'] = json_dict_main_2
                    json_dic_main_main['3'] = json_dict_main_3
                    json_dic_main_main['4'] = json_dict_main_4
                    json_dic_main_main['5'] = json_dict_main_5

                # открываем файл json_timetable.json для записи json_dic_main_main(итога)
                with open("json_timetable.json", "w", encoding="utf-8") as file:
                    # Запись в json-file словаря
                    json.dump(json_dic_main_main, file, indent=4, ensure_ascii=False, separators=(',', ': '))

                time_table.close()  # Закрываем текстовый файл.
            except IOError:
                print("Ошибка открытия файла IOError!")
        elif time_table_file_name.split('.')[1] == 'xlsx':
            work_book = load_workbook(filename=self.time_table_file_name)
            sheet = work_book['Лист1']
            not_empty = True
            line = 1
            date = str(sheet[f'A{line}'].value).split()[0]
            json_dict_main_1 = dict()  # создание словаря для заполнения одного отряда
            json_dict_main_2 = dict()  # создание словаря для заполнения одного отряда
            json_dict_main_3 = dict()  # создание словаря для заполнения одного отряда
            json_dict_main_4 = dict()  # создание словаря для заполнения одного отряда
            json_dict_main_5 = dict()  # создание словаря для заполнения одного отряда  # создание словаря для заполнения одного отряда
            json_dic_main_main = dict()  # итоговый словарь
            dict_for_the_day_1 = dict()  # обновляем словарь дня
            dict_for_the_day_2 = dict()  # обновляем словарь дня
            dict_for_the_day_3 = dict()  # обновляем словарь дня
            dict_for_the_day_4 = dict()  # обновляем словарь дня
            dict_for_the_day_5 = dict()  # обновляем словарь дня
            blank_lines = 0
            while not_empty:
                if len(str(sheet[f'A{line}'].value).split()) == 2:
                    json_dict_main_1[date] = dict_for_the_day_1  # в словарь расписания отряда записываем словварь дня
                    json_dict_main_2[date] = dict_for_the_day_2  # в словарь расписания отряда записываем словварь дня
                    json_dict_main_3[date] = dict_for_the_day_3  # в словарь расписания отряда записываем словварь дня
                    json_dict_main_4[date] = dict_for_the_day_4  # в словарь расписания отряда записываем словварь дня
                    json_dict_main_5[date] = dict_for_the_day_5  # в словарь расписания отряда записываем словварь дня

                    dict_for_the_day_1 = dict()  # обновляем словарь дня
                    dict_for_the_day_2 = dict()  # обновляем словарь дня
                    dict_for_the_day_3 = dict()  # обновляем словарь дня
                    dict_for_the_day_4 = dict()  # обновляем словарь дня
                    dict_for_the_day_5 = dict()  # обновляем словарь дня
                    date = str(sheet[f'A{line}'].value).split()[0]  # увеличиваем дату
                    line += 1
                elif sheet[f'A{line}'].value is None:
                    blank_lines += 1
                    if blank_lines == 2:
                        not_empty = False
                else:
                    time_start = str(sheet[f'A{line}'].value)[:5]
                    time_finish = str(sheet[f'B{line}'].value)[:5]
                    time = f'{time_start}-{time_finish}'
                    activity = sheet[f'C{line}'].value
                    if activity.lower() == 'обед' or activity.lower() == 'ужин' or activity.lower() == 'завтрак' or activity.lower() == 'сонник' or activity.lower() == 'полдник':
                        dict_for_the_day_1[time_formatted_for_groups(f'{time_start}-{time_finish}',
                                                                     1)] = activity  # Добавляем в словарь дня время и занятие в это время
                        dict_for_the_day_2[time_formatted_for_groups(f'{time_start}-{time_finish}',
                                                                     2)] = activity  # Добавляем в словарь дня время и занятие в это время
                        dict_for_the_day_3[time_formatted_for_groups(f'{time_start}-{time_finish}',
                                                                     3)] = activity  # Добавляем в словарь дня время и занятие в это время
                        dict_for_the_day_4[time_formatted_for_groups(f'{time_start}-{time_finish}',
                                                                     4)] = activity  # Добавляем в словарь дня время и занятие в это время
                        dict_for_the_day_5[time_formatted_for_groups(f'{time_start}-{time_finish}',
                                                                     5)] = activity  # Добавляем в словарь дня время и занятие в это время
                    else:
                        dict_for_the_day_1[time] = activity  # Добавляем в словарь дня время и занятие в это время
                        dict_for_the_day_2[time] = activity  # Добавляем в словарь дня время и занятие в это время
                        dict_for_the_day_3[time] = activity  # Добавляем в словарь дня время и занятие в это время
                        dict_for_the_day_4[time] = activity  # Добавляем в словарь дня время и занятие в это время
                        dict_for_the_day_5[time] = activity  # Добавляем в словарь дня время и занятие в это время
                    blank_lines = 0
                    line += 1

            json_dic_main_main['1'] = json_dict_main_1
            json_dic_main_main['2'] = json_dict_main_2
            json_dic_main_main['3'] = json_dict_main_3
            json_dic_main_main['4'] = json_dict_main_4
            json_dic_main_main['5'] = json_dict_main_5
            with open("json_timetable.json", "w", encoding="utf-8") as file:
                # Запись в json-file словаря
                json.dump(json_dic_main_main, file, indent=4, ensure_ascii=False, separators=(',', ': '))