from configparser import ConfigParser
import os

# Компании: Авито, Яндекс, МТС Банк, Лаборатория Касперского, Tinkoff, РЖД, Аэрофлот, Альфа-банк, Озон, СБЕР
employer_ids = [84585, 1740, 4496, 1057, 78638, 23427, 1373, 80, 2180, 3529]

JSON_DATA = os.path.join('data')
JSON_FILE_NAME = 'data.json'


def config(filename: str = "data/database.ini", section: str = "postgresql"):
    """
    Получает параметры базы данных

    """

    path_absolute = os.path.abspath(filename)
    parser = ConfigParser()

    parser.read(path_absolute)
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception(
            'Section {0} is not found in the {1} file.'.format(section, filename))
    return db
