
from src.data_cleaner import load_and_clean_data

from src.analyzer import(
    base_stat,
    top_genres,
    streaming_service_stats,
    genre_analysis,
    working_analysis,
    hours_correlation,
    numpy_stats,
    make_conclusions,
)

def test_base_stat():
    data = load_and_clean_data()
    stats = base_stat(data)
    assert isinstance(stats, dict)
    assert "средний возраст" in stats
    assert "среднее число прослушиваний в день" in stats
    assert "средний показатель тревоги" in stats
    assert "средний показатель депрессии" in stats
    assert "средний показатель бессонницы" in stats
    assert "средний показатель ОКР" in stats

def test_top_genres_not_empty():
    data = load_and_clean_data()
    top = top_genres(data)
    assert len(top) > 0

def test_streaming_service_stats_not_empty():
    data = load_and_clean_data()
    stats = streaming_service_stats(data)
    assert len(stats) > 0

def test_hours_correlation():
    data = load_and_clean_data()
    corr = hours_correlation(data)
    assert "Anxiety" in corr
    assert "Depression" in corr
    assert "Insomnia" in corr
    assert "OCD" in corr

def test_numpy_stats_returns_dict():
    data = load_and_clean_data()
    result = numpy_stats(data)
    assert isinstance(result, dict)

def test_make_conclusions_returns_list():
    data = load_and_clean_data()
    conclusions = make_conclusions(data)
    assert isinstance(conclusions, list)