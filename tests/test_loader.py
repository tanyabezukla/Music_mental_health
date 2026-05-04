
from src.data_loader import load_data

def test_load_data_not_empty():
    df = load_data()
    assert len(df) > 0, "DataFrame should not be empty"

