from src.DBManager import DBManager
from utils import user_interaction
from config import JSON_FILE_NAME, employer_ids
from src.headhunter import HeadHunter_API
from sql.db_create import create_tables, insert_to_employers, insert_to_vacancies


def main():
    hh = HeadHunter_API()
    vacancies_list = hh.get_vacancies_by_api(employer_ids)
    hh.save_vacancies_to_json(vacancies_list, JSON_FILE_NAME)

    while 1:
        db_name = input('Введите слово на английском для названия базы данных: ')
        if all(one_letter in 'abcdefghijklmnopqrstuvwxyz1234567890' for one_letter in db_name):
            db = DBManager()
            break
        else:
            print("Введите слово на английском")
    # создание базы данных
    db.create_database(db_name)
    # создание таблицы в базе данных
    db.create_table(create_tables)
    # заполняем таблицы
    db.insert_data_to_table(JSON_FILE_NAME, insert_to_employers, insert_to_vacancies)

    # работаем с выборками в БД
    user_interaction(db)


if __name__ == 'main':
    main()