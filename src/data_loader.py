import pandas as pd


def load_data():
    data = pd.read_csv("data\mxmh_survey_results.csv")
    df = pd.DataFrame(data)
    return df

