from src.data_loader import load_data
from src.data_cleaner import load_and_clean_data
from src.analyzer import base_stat, top_genres, streaming_service_stats, genre_analysis, working_analysis, hours_correlation, numpy_stats


def show_raw_data_info(raw_data):
    
    

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



def show_cleaned_data_info(cleaned_data):


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

    print(cleaned_data.dtypes)


def main():

    # raw_data = load_data()
    cleaned_data = load_and_clean_data()

    # show_raw_data_info(raw_data)
    show_cleaned_data_info(cleaned_data)

    # base_stat(cleaned_data)
    # genre_analysis(cleaned_data)
    # working_analysis(cleaned_data)
    # hours_analysis(cleaned_data)
    # print(numpy_stats(cleaned_data))


if __name__ == "__main__":
    main()


