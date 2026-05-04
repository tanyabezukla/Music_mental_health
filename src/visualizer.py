
from pathlib import Path
import matplotlib.pyplot as plt

def plot_top_genres(data):
    genre_counts = data["Fav genre"].value_counts().head(10)

    plots_dir = Path(__file__).resolve().parent.parent / "plots"
    plots_dir.mkdir(exist_ok=True)

    plt.figure(figsize=(10, 6))
    genre_counts.plot(kind="bar")
    plt.title("Топ-10 любимых жанров")
    plt.xlabel("Жанр")
    plt.ylabel("Количество респондентов")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(plots_dir / "top_genres.png")
    plt.close()

def plot_streaming_services(data):
    #Строит график популярных стриминговых сервисов.
    service_counts = data["Primary streaming service"].value_counts()

    plots_dir = Path(__file__).resolve().parent.parent / "plots"
    plots_dir.mkdir(exist_ok=True)

    plt.figure(figsize=(10, 6))
    service_counts.plot(kind="bar")
    plt.title("Популярность стриминговых сервисов")
    plt.xlabel("Сервис")
    plt.ylabel("Количество респондентов")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(plots_dir / "streaming_services.png")
    plt.close()

def plot_music_effects(data):
    #Строит круговую диаграмму влияния музыки на состояние
    effects_counts = data["Music effects"].value_counts()

    plots_dir = Path(__file__).resolve().parent.parent / "plots"
    plots_dir.mkdir(exist_ok=True)

    plt.figure(figsize=(8, 8))
    effects_counts.plot(kind="pie", autopct="%1.1f%%")
    plt.title("Влияние музыки на состояние")
    plt.ylabel("")
    plt.tight_layout()
    plt.savefig(plots_dir / "music_effects.png")
    plt.close()

def build_all_plots(data):
    #Создаёт все графики сразу
    plot_top_genres(data)
    plot_streaming_services(data)
    plot_music_effects(data)
    