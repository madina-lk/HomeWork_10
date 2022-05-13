from flask import Flask
from utils import *

app = Flask(__name__)


@app.route("/")
def show_persons():
    """Представление для роута для вывода полей списка словаря с индексами name, position, skills """

    persons = ""

    for person in get_json_load('candidates.json'):     # перебор элементов json-файла
        persons += get_person_data(person)              # занесение полученных данных в переменную persons

    return f'<pre>{persons}</pre>'


@app.route('/candidates/<int:id>')
def get_profile(id):
    """Представление для роута candidates/<x> для вывода информации о кандидате и изображение"""

    persons = ""
    img_url = ""

    for person in get_json_load('candidates.json'):      # перебор элементов json-файла
        if person['id'] == id:                           # условие проверки id
            persons = get_person_data(person)            # занесение полученных данных в переменную persons
            img_url = person["picture"]                  # получение ссылки на картинку

    return f'<img src={img_url}><br/> <pre>{persons}</pre>'


@app.route('/skills/<skill>')
def get_skills(skill):
    """Представление /skills/<x> для поиска по навыкам.
     Выводит тех кандидатов, в списке навыков у которых содержится skill
     """

    persons = ""

    for person in get_json_load('candidates.json'):     # перебор элементов json-файла
        if skill in person['skills']:                   # условие проверки skills
            persons += get_person_data(person)          # занесение полученных данных в переменную persons

    return f'<pre>{persons}</pre>'


app.run()




