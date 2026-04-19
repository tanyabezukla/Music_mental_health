
from src.data_loader import load_data

data = load_data()

print("\nПервые 5 строк:")
print(data.head())

print("\nИнформация о таблице:")
print(data.info())

print("\n Названия столбцов")
print(data.columns)

print("\nКоличество пропусков в каждом столбце:")
print(data.isnull().sum())
