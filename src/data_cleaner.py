import pandas as pd

from src.data_loader import load_data


def load_and_clean_data() :
    
    df = load_data().copy()
    df = df.drop_duplicates()
    


    #приводим важные столбцы к числовому, если там не число то Nan
    df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
    df["Hours per day"] = pd.to_numeric(df["Hours per day"], errors="coerce")
    df["BPM"] = pd.to_numeric(df["BPM"], errors="coerce")

    df = df.dropna(subset=["Age"])
    df = df[(df["Age"] >= 10) & (df["Age"] <= 80)]

    #заполняем пропуски в текстовых столбцах
    df["Primary streaming service"] = df["Primary streaming service"].fillna("Unknown")
    df["While working"] = df["While working"].fillna("Unknown")
    df["Instrumentalist"] = df["Instrumentalist"].fillna("Unknown")
    df["Composer"] = df["Composer"].fillna("Unknown")
    df["Foreign languages"] = df["Foreign languages"].fillna("Unknown")
    df["Music effects"] = df["Music effects"].fillna("Unknown")


    #заполняем медианой
    df["BPM"] = df["BPM"].fillna(df["BPM"].median())
    df["Hours per day"] = df["Hours per day"].fillna(df["Hours per day"].median())

    return df
