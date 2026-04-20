import pandas as pd 

def base_stat(data):
    print("\nБазовая статистика")

    print(f"\nСредний возраст: {data['Age'].mean():.2f}")
    print(f"Среднее количество часов прослушивания в день: {data['Hours per day'].mean():.2f}")

    print("\n Средние показатели психического состояния")
    print(f"Anxiety: {data['Anxiety'].mean():.2f}")
    print(f"Depression: {data['Depression'].mean():.2f}")
    print(f"Insomnia: {data['Insomnia'].mean():.2f}")
    print(f"OCD: {data['OCD'].mean():.2f}")

    print("\n Самые популярные жанры")
    print(data["Fav genre"].value_counts().head(5))

    print("\nМузыка во время работы:")
    print(data['While working'].value_counts())


    