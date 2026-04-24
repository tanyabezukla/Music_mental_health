
from src.data_cleaner import load_and_clean_data
from src.analyzer import base_stat, genre_analysis, make_conclusions

df = load_and_clean_data()

print(base_stat(df))
print(genre_analysis(df).head())
print(make_conclusions(df))