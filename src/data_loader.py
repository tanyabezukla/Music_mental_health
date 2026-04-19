from pathlib import Path

import pandas as pd


def load_data() -> pd.DataFrame:
    """Load the survey dataset and return it as a DataFrame."""
    project_root = Path(__file__).resolve().parent.parent
    data_path = project_root / "data" / "mxmh_survey_results.csv"
    return pd.read_csv(data_path)
