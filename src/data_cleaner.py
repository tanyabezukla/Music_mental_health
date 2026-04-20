import pandas as pd

from src.data_loader import load_data


def load_and_clean_data() -> pd.DataFrame:
    """Load the dataset, remove duplicates, and fill missing values."""
    df = load_data().copy()
    df = df.drop_duplicates()
    df = df.dropna(how="all")

    numeric_columns = df.select_dtypes(include=["number"]).columns
    for column in numeric_columns:
        df[column] = df[column].fillna(df[column].median())

    categorical_columns = df.select_dtypes(include=["object"]).columns
    for column in categorical_columns:
        mode = df[column].mode(dropna=True)
        fill_value = mode.iloc[0] if not mode.empty else "Unknown"
        df[column] = df[column].fillna(fill_value)

    return df
