def get_json_load(filename):
    """Выгружает данные из файла .json"""

    import json
    file = open(filename, encoding="utf-8")                 # открытие json - файла

    return json.load(file)                                  # загрузка списка словарей из json - файла


def get_person_data(data_list):
    """Получение информации об имени кандидата, пизиции и навыков в заданном формате"""

    return '\nИмя кандидата - ' + data_list['name'] + \
           '\nПозиция кандидата: ' + data_list['position'] + \
           '\nНавыки: ' + data_list['skills'] + \
           '\n'



