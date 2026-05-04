
from src.data_cleaner import load_and_clean_data

def test_clean_data_not_empty():
    df = load_and_clean_data()
    assert len(df) > 0, "DataFrame should not be empty"

def test_cleaan_data_age_has_no_missing_values():
    df = load_and_clean_data()
    assert df["Age"].isnull().sum() == 0, "Age column should not have missing values"

def test_clean_data_age_in_valid_range():
    df = load_and_clean_data()
    assert df["Age"].min() >= 10
    assert df["Age"].max() <= 80
