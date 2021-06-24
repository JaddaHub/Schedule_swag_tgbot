import json

json_path = 'users_data.json'


def get_squad(id_):
    with open(json_path, encoding='utf-8') as js_file:
        users_data = json.load(js_file)
        return users_data.get(id_, False)


def set_squad(id_, squad):
    with open(json_path, encoding='utf-8') as js_file:
        user_data = json.load(js_file)
        user_data[id_] = squad

        with open(json_path, 'w', encoding='utf-8') as js_dump:
            json.dump(user_data, js_dump)


def __clear_json():
    with open(json_path, 'w', encoding='utf-8') as js_file:
        json.dump(dict(), js_file)

