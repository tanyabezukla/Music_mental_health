import pandas as pd


def load_data():
    try:
        data = pd.read_csv("data/mxmh_survey_results.csv")
        df = pd.DataFrame(data)
        return df
    
    except FileNotFoundError:
        print("Файл не найден. Проверьте путь к файлу")
        raise

    except pd.errors.EmptyDataError:
        print("Файл пустой. Проверьте содержимое файла")
        raise

    except pd.errors.ParserError:
        print("Ошибка парсинга. Проверьте формат файла")
        raise





