from src.analyzer import base_stat, top_genres


def insight_generator(insights):
    for insight in insights:
        yield insight


def report_generator(data):
    yield "ОТЧЁТ ПО АНАЛИЗУ ДАННЫХ"
    yield "Базовая статистика:"

    stats = base_stat(data)
    yield f"Средний возраст: {stats['средний возраст']}"
    yield f"Средние часы прослушивания: {stats['среднее число прослушиваний в день']}"
    yield f"Средний уровень тревоги: {stats['средний показатель тревоги']}"
    yield f"Средний уровень депрессии: {stats['средний показатель депрессии']}"
    yield f"Средний уровень бессонницы: {stats['средний показатель бессонницы']}"
    yield f"Средний уровень ОКР: {stats['средний показатель ОКР']}"

    yield ""
    yield "Топ жанров:"

    top_genres_stats = top_genres(data, 5)
    for genre, count in top_genres_stats.items():
        yield f"{genre}: {count} респондентов"
