import pandas as pd 
import numpy as np


# def base_stat(data):
#     print("\nБазовая статистика")

#     print(f"\nСредний возраст: {data['Age'].mean():.2f}")
#     print(f"Среднее количество часов прослушивания в день: {data['Hours per day'].mean():.2f}")

#     print("\n Средние показатели психического состояния")
#     print(f"Anxiety: {data['Anxiety'].mean():.2f}")
#     print(f"Depression: {data['Depression'].mean():.2f}")
#     print(f"Insomnia: {data['Insomnia'].mean():.2f}")
#     print(f"OCD: {data['OCD'].mean():.2f}")

#     print("\n Самые популярные жанры")
#     print(data["Fav genre"].value_counts().head(5))

#     print("\nМузыка во время работы:")
#     print(data['While working'].value_counts())

def base_stat(data):
    stats = {
        "средний возраст" : round(data['Age'].mean(), 2),
        "среднее число прослушиваний в день": round(data['Hours per day'].mean(), 2),
        "средний показатель тревоги": round(data['Anxiety'].mean(), 2),
        "средний показатель тревоги": round(data['Depression'].mean(), 2),
        "средний показатель бессоницы": round(data['Insomnia'].mena(), 2),
        "средний показатель ОКР": round(data['OCD'].mean(), 2),
    }
    return stats


def top_genres(data, n):
    return data["Fav genre"].value_counts().head(n)


def streaming_service_stats(data):
    return data["Primary streaming service"].value_counts()


def genre_analysis(data):
    #средние показатели психического здоровья по любимому жанру
    genre_stats = data.groupby("Fav genre")[["Anxiety", "Depression", "Insomnia", "OCD"]].mean()

    return genre_stats.sort_values("Anxiety", ascending=False)


def working_analysis(data):

    #сравнение психического состояния между теми кто слушает музыку во время работы и теми кто не слушеат
    work_stats = data.groupby("While working")[["Anxiety", "Depression", "Insomnia", "OCD", "Hours per day"]].mean()
    return work_stats.sort_values("Anxiety", ascending = False)

def hours_correlation(data):
    #Связь числа прослушиваний и состояний
    corr = data[["Hours per day","Anxiety", "Depression", "Insomnia", "OCD"]].corr()
    return corr["Hours per day"].drop("Hours per day") #корреляция только с количеством часов прослушивания

def numpy_stats(data):
    hours = data["Hours per day"].to_numpy()
    anxiety = data["Anxiety"].to_numpy()
    depression = data["Depression"].to_numpy()

    stats = {
        "Среднее количество часов прослушивания в день": round(np.mean(hours), 2),
        "Насколько разбросаны значения часов прослушивания": round(np.std(hours), 2),
        "Средний уровень тревоги": round(np.mean(anxiety), 2),
        "Насколько разбросаны значения уровня тревоги": round(np.std(anxiety), 2),
        "Средний уровень депрессии": round(np.mean(depression), 2),
        "Насколько разбросаны значения уровня депрессии": round(np.std(depression), 2),
    }

    return stats

def make_conclusions(data):
    conclusions = []

    #1. Самый популярный жанр
    most_popular_genre = data["Fav genre"].value_counts().idxmax()
    conclusions.append(f"Самый популярный жанр: {most_popular_genre}")

    #2. Самый популярный стриминг сервис
    most_common_streaming = data["Primary streaming service"].value_counts().idxmax()
    conclusions.append(f"Самый популярный стриминг сервис: {most_common_streaming}")

    #3. Слушают ли люди музыку во время работы
    working_counts = data["While working"].value_counts()
    if "Yes" in working_counts.index and "No" in working_counts.index:
        if working_counts["Yes"] > working_counts["No"]:
            conclusions.append("Большинство людей слушают музыку во время работы")
        else:
            conclusions.append("Большинство людей не слушают музыку во время работы")

    #5 как люди оценивают влияние музыки
    effect_counts = data["Music effects"].value_counts()
    if "Improve" in effect_counts.index:
        improve_share = effect_counts["Improve"] / effect_counts.sum()
        conclusions.append(f"{improve_share:.2%} респондентов считают, что музыка улучшает их психическое состояние")
    
    #6 самая сильная связь 
    corr = hours_correlation(data)
    strongest_corr = corr.abs().idxmax()
    conclusions.append(f"Самая сильная связь с количеством часов прослушивания у показателя: {strongest_corr}")

    #7 жанр с самым высоким средним  уровнем тревоги
    genre_stats = genre_analysis(data)
    top_anxiety_genre = genre_stats["Anxiety"].idxmax()
    conclusions.append(f"Жанр с самым высоким средним уровнем тревоги: {top_anxiety_genre}")

    top_insomnia_genre = genre_stats["Insomnia"].idxmax()
    conclusions.append(f"Жанр с самым высоким средним уровнем бессоницы: {top_insomnia_genre}")

    # 8  показатель в среднем самый высокий
    mean_scores = {
        "Anxiety": data["Anxiety"].mean(),
        "Depression": data["Depression"].mean(),
        "Insomnia": data["Insomnia"].mean(),
        "OCD": data["OCD"].mean(),
    }
    highest_score = max(mean_scores, key=mean_scores.get)
    conclusions.append(f"В среднем самый высокий показатель в выборке: {highest_score}.")

    #9 у какого жанра самый большой и смаыймаленький срелний возраст
    age_by_genre = data.groupby("Fav genre")["Age"].mean()
    oldest_genre = age_by_genre.idxmax()
    youngest_genre = age_by_genre.idxmin()
    conclusions.append(f"Жанр с самым высоким средним возрастом: {oldest_genre}")
    conclusions.append(f"Жанр с самым низким средним возрастом: {youngest_genre}")

    return conclusions