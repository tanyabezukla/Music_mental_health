import argparse

from src.analyzer import (
    base_stat,
    genre_analysis,
    hours_correlation,
    make_conclusions,
    numpy_stats,
    streaming_service_stats,
    top_genres,
    working_analysis,
)
from src.data_cleaner import load_and_clean_data
from src.generators import report_generator

from src.visualizer import build_all_plots


def print_mapping(mapping):
    for key, value in mapping.items():
        print(f"{key}: {value}")


def main():
    parser = argparse.ArgumentParser(
        description="Анализ данных опроса о музыкальных предпочтениях"
    )
    parser.add_argument(
        "command",
        choices=["stats", "analyze", "report", "genres", "services", "plot"],
        help="команда для выполнения",
    )
    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
        return

    data = load_and_clean_data()

    if args.command == "stats":
        print("Базовая статистика:")
        print_mapping(base_stat(data))
        print("\nСтатистика numpy:")
        print_mapping(numpy_stats(data))

    elif args.command == "analyze":
        print("Анализ по жанрам:")
        print(genre_analysis(data).head(10))

        print("\nМузыка во время работы:")
        print(working_analysis(data))

        print("\nКорреляция между часами прослушивания и состояниями:")
        print(hours_correlation(data))

        print("\nВыводы:")
        insights = make_conclusions(data)
        for insight in insights:
            print(f"- {insight}")

    elif args.command == "report":
        print("Генерация отчета:")
        for line in report_generator(data):
            print(line)

    elif args.command == "genres":
        print("Топ жанров:")
        print(top_genres(data, 10))

    elif args.command == "services":
        print("Статистика по стриминговым сервисам:")
        print(streaming_service_stats(data))

    elif args.command == "plot":
        build_all_plots(data)
        print("Графики сохранены в папке plots")


if __name__ == "__main__":
    main()
