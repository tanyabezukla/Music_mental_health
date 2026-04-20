import pandas as pd

from src.data_loader import load_data


def load_and_clean_data() -> pd.DataFrame:
    """загружаем сет, удаляем дубликаты, заполняем пропуски"""
    df = load_data().copy()
    df = df.drop_duplicates()
    df = df.dropna(subset=["Age"])

    df["Primary streaming service"] = df["Primary streaming service"].fillna("Unknown")
    df["While working"] = df["While working"].fillna("Unknown")
    df["Instrumentalist"] = df["Instrumentalist"].fillna("Unknown")
    df["Composer"] = df["Composer"].fillna("Unknown")
    df["Foreign languages"] = df["Foreign languages"].fillna("Unknown")
    df["Music effects"] = df["Music effects"].fillna("Unknown")


    # заполняем BPM медианой
    df["BPM"] = df["BPM"].fillna(df["BPM"].median())
    return df
