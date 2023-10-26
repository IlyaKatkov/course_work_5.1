from sql.db_create import get_all_employers_query, get_all_vacancies_query, get_avg_salary_query, get_high_salary_query


def user_interaction(db_manager):
    """
    Происходит взаимодействие с пользователем
    """
    user_input_1 = input('показать все компании и количество вакансий от каждого из них? (1 - да): ')
    if user_input_1 == '1':
        list_employers_and_vacancies_count = db_manager.get_companies_and_vacancies_count(get_all_employers_query)
        for one_employer in list_employers_and_vacancies_count:
            print(f'Получено {one_employer[1]} вакансий от работодателя {one_employer[0]}')
    else:
        input('Для продолжения нажмите любую клавишу')

    user_input_2 = input('показать все компании и количество вакансий от каждого из них? (1 - да): ')
    if user_input_2 == '1':
        all_vacancies_list = db_manager.get_all_vacancies(get_all_vacancies_query)
        for one_vacancy in all_vacancies_list:
            print(*one_vacancy, sep=' | ')
    else:
        input('Для продолжения нажмите любую клавишу')

    user_input_3 = input('Показать среднюю зарплату по всем вакансиям? (1 - да): ')
    if user_input_3 == '1':
        print(f'\nСредняя зарплата по вакансиям равна {db_manager.get_avg_salary(get_avg_salary_query)} руб.\n')
    else:
        input('Для продолжения нажмите любую клавишу')

    user_input_4 = input('Показать вакансии с зарплатой выше средней? (1 - да): ')
    if user_input_4 == '1':
        print('\nВот наиболее высокооплачиваемые вакансии:\n')
        vacancies_with_high_salary = db_manager.get_vacancies_with_higher_salary(get_high_salary_query)
        for one_vacancy in vacancies_with_high_salary:
            print(*one_vacancy, sep=' | ')
    else:
        input('Для продолжения нажмите любую клавишу')

    keyword = input('Введите ключевое слово для поиска вакансий: ')
    if keyword:
        vacancies_with_keyword = db_manager.get_vacancies_with_keyword(keyword)
        if vacancies_with_keyword:
            print('\nВот вакансии по вашему запросу:\n')
            for one_vacancy in vacancies_with_keyword:
                print(*one_vacancy, sep=' | ')
        else:
            print('По вашему запросу нет вакансий')

    else:
        exit('Опций больше нет')