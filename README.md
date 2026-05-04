# Music Mental Health

Проект анализирует данные опроса о музыкальных привычках и показателях психического состояния.  
В датасете используются ответы респондентов о любимых жанрах, времени прослушивания музыки, стриминговых сервисах и самооценке тревоги, депрессии, бессонницы и ОКР.

## Возможности

- загрузка CSV-датасета;
- очистка данных: удаление дубликатов, обработка пропусков, приведение числовых колонок к числам;
- фильтрация некорректного возраста;
- базовая статистика по возрасту, часам прослушивания и показателям состояния;
- анализ любимых жанров и стриминговых сервисов;
- расчет корреляции между временем прослушивания музыки и показателями состояния;
- генерация текстового отчета;
- тесты для загрузчика, очистки данных и аналитических функций.

## Структура проекта

```text
Music_mental_health/
├── data/
│   └── mxmh_survey_results.csv
├── src/
│   ├── __init__.py
│   ├── analyzer.py
│   ├── data_cleaner.py
│   ├── data_loader.py
│   ├── decorators.py
│   └── generators.py
├── tests/
│   ├── test_analyzer.py
│   ├── test_cleaner.py
│   └── test_loader.py
├── main.py
├── pytest.ini
├── requirements.txt
└── README.md
```

## Установка

Перейдите в папку проекта:

```powershell
cd C:\Users\Admin\Desktop\project_music_mental\Music_mental_health
```

Создайте и активируйте виртуальное окружение:

```powershell
python -m venv .venv
.\.venv\Scripts\activate
```

Установите зависимости:

```powershell
pip install -r requirements.txt
```

## Запуск

Посмотреть доступные команды:

```powershell
python main.py
```

Базовая статистика:

```powershell
python main.py stats
```

Полный анализ:

```powershell
python main.py analyze
```

Текстовый отчет:

```powershell
python main.py report
```

Топ жанров:

```powershell
python main.py genres
```

Статистика по стриминговым сервисам:

```powershell
python main.py services
```

## Тесты

Запуск всех тестов:

```powershell
python -m pytest
```

Ожидаемый результат:

```text
10 passed
```

## Основные модули

- `src/data_loader.py` загружает датасет из `data/mxmh_survey_results.csv`.
- `src/data_cleaner.py` очищает данные и подготавливает их к анализу.
- `src/analyzer.py` содержит функции статистики и анализа.
- `src/generators.py` формирует текстовый отчет.
- `main.py` предоставляет CLI-интерфейс для запуска анализа.

## Данные

Файл данных должен находиться по пути:

```text
data/mxmh_survey_results.csv
```

Если файл будет перемещен или переименован, нужно обновить путь в `src/data_loader.py`.
