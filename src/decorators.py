import time
from functools import wraps


def log_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Функция запущена:", func.__name__)
        return func(*args, **kwargs)

    return wrapper


def measure_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(
            "Время выполнения функции",
            func.__name__,
            ":",
            round(end_time - start_time, 4),
            "сек.",
        )
        return result

    return wrapper
