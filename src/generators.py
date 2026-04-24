import pandas as pd
from src.analyzer import base_stat, top_genres

def insight_generator(insights):
    for insight in insights:
        yield insight

def report_generator(data):
    yield "ОТЧЁТ ПО АНАЛИЗУ ДАННЫХ"
    yield "Базовая статистика:"
    stats = base_stat(data)
    yield f"Средний возраст: {stats['mean_age']}"
    yield f"Средние часы прослушивания: {stats['mean_hours']}"
    yield f"Средний уровень тревоги: {stats['mean_anxiety']}"
    yield f"Средний уровень депрессии: {stats['mean_depression']}"      
    yield f"Средний уровень бессонницы: {stats['mean_insomnia']}"
    yield f"Средний уровень ОКР: {stats['mean_OCD']}"
    yield ""
    yield "Топ жанров:"
    top_genres = top_genres(data, 5)
    for genre, count in top_genres.items():
        yield f"{genre}: {count} респондентов"  

