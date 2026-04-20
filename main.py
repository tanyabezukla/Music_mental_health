from src.data_loader import load_data
from src.data_cleaner import load_and_clean_data
from src.analyzer import base_stat

raw_data = load_data()
cleaned_data = load_and_clean_data()

print("\nИсходные данные: первые 5 строк")
print(raw_data.head())

print("\nИсходные данные: информация о таблице")
raw_data.info()

print("\nИсходные данные: названия столбцов")
print(raw_data.columns)

print("\nИсходные данные: количество пропусков")
print(raw_data.isnull().sum())

print("\nИсходные данные: размер таблицы")
print(raw_data.shape)

print("\nИсходные данные: количество дубликатов")
print(raw_data.duplicated().sum())

print("\nОчищенные данные: первые 5 строк")
print(cleaned_data.head())

print("\nОчищенные данные: информация о таблице")
cleaned_data.info()

print("\nОчищенные данные: количество пропусков")
print(cleaned_data.isnull().sum())

print("\nОчищенные данные: размер таблицы")
print(cleaned_data.shape)

print("\nОчищенные данные: количество дубликатов")
print(cleaned_data.duplicated().sum())

base_stat(cleaned_data)


