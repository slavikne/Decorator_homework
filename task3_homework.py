import datetime
geo_log = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]
def decor_log(path):
    def _decor_log(old_function):
        def new_function(*args, **kwargs):
            now = datetime.datetime.now()
            result = old_function(*args, **kwargs)
            with open(path, 'w', encoding='utf-8') as file:
                file.write(f'Функция: {old_function.__name__}\nвызвана: {now}\nc аргументами: {args} {kwargs}\n'
                           f'возвращаемое значение: {result} ')
            return result
        return new_function
    return _decor_log


@decor_log('function_log.log')
def geo_logs(geo_logs):
    geo_logs_rus = []
    for visits in geo_logs:
        for city, country in visits.values():
            if country == 'Россия':
                geo_logs_rus.append(visits)
    return geo_logs_rus

geo_logs(geo_log)