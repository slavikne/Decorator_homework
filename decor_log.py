import datetime

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
def foo(a,b,c):
    return a * b + c

foo(4,5,8)