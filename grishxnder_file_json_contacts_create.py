import json
dict_contacts = {
    "Организаторы": "Почта - mail@innopoliscamp.ru \n"
                    "Контактный номер - 8-965-583-19-27 \n"
                    "Адрес - г. Иннополис, ул. Квантовый бульвар, д.1, здание Лицея Иннополис.",
    "Преподователи": "У InnoCamp 11 преподователей по направлениям: \n"
                     "Камилла Хамидуллина - @Kamila_ak \n"
                     "Макше Сейткалиев - @seytkalievm \n"
                     "Маргарита Сидорская - @RitaSidorskya \n"
                     "Никита Носков - @MPardis \n"
                     "Артем Сахаров - @ilostmygoddamnson \n"
                     "Артемий Кочергин - @treatn \n"
                     "Динар Шамсутдинов - @d_shamik \n"
                     "Марина Лебединская - @mari1861 \n"
                     "Анастасия Андронова - @andronova_anastasia \n"
                     "Макар Шевченко - @SyrexMinus \n"
                     "Евгений Сазонов - @EvgenySazonov",
    "Вожатые": "1 отряд: Вова и Юля \n"
               "2 отряд:  \n"
               "3 отряд:  \n"
               "4 отряд:  \n"
               "5 отряд: ",
    "Остальные": "DJ(диджей) - Виталий - +79047674852"
}

with open("json_contacts.json", "w", encoding="utf-8") as file:
    json.dump(dict_contacts, file, indent=4, ensure_ascii=False, separators=(',', ': '))