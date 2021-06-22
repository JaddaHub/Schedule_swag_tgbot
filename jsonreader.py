import json


def set_otryad(id_, otryad_):
    try:
        dictData = {"ID": id_,
                    "otryad": otryad_}
        jsonData = json.dumps(dictData)
        with open("ids/" + str(id_) + ".json", "w") as file:
            file.write(jsonData)
        # print(jsonData)
        return True
    except:
        return False


def get_otryad(id_):
    try:
        with open("ids/" + str(id_) + ".json", "r+") as file:
            jsonData = file.read()
            dictData = json.loads(jsonData)
        return dictData["otryad"]
    except:
        return None
