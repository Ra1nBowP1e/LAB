import csv

def analyze_csv_no_pandas(filepath):
    """Анализирует CSV-файл без использования pandas, используя столбец 'Price'."""
    try:
        with open(filepath, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            data = list(reader)

            if not data:
                print("Файл пустой.")
                return

            print("Содержимое файла (Ключ → Значение):")
            for row in data:
                print(row)

            prices = [float(row['Price']) for row in data if 'Price' in row and row['Price'].replace('.','',1).isdigit()]

            if not prices:
                print("\nСтолбец 'Price' не найден или содержит нечисловые данные.")
                return

            min_price = min(prices)
            max_price = max(prices)
            sum_prices = sum(prices)
            avg_price = sum_prices / len(prices)


            print(f"\nМинимальная цена (Price): {min_price}")
            print(f"Максимальная цена (Price): {max_price}")
            print(f"Средняя цена (Price): {avg_price}")

    except FileNotFoundError:
        print(f"Файл {filepath} не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")




filepath = "4.csv"  # Замените на путь к вашему файлу
analyze_csv_no_pandas(filepath)




import json
import os

def analyze_json(filepath, version_prefix, output_filepath="out.json"):
    """
    Анализирует JSON-файл, находит пользователей по префиксу номера версии и сохраняет результаты.

    Args:
        filepath: Путь к входному JSON-файлу.
        version_prefix: Префикс номера версии для поиска (строка).
        output_filepath: Путь к выходному JSON-файлу (по умолчанию "out.json").
    """
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)

        if not isinstance(data, list):
            print("Ошибка: JSON-файл должен содержать список объектов.")
            return

        filtered_data = [user for user in data if user.get('version').startswith(version_prefix + ".")]

        if not filtered_data:
            print(f"Пользователи с версией, начинающейся с {version_prefix}. не найдены.")
        else:
            os.makedirs(os.path.dirname(output_filepath), exist_ok=True)
            with open(output_filepath, 'w') as outfile:
                json.dump(filtered_data, outfile, indent=4)
            print(f"Отфильтрованные данные сохранены в файл {output_filepath}")

    except FileNotFoundError:
        print(f"Файл {filepath} не найден.")
    except json.JSONDecodeError:
        print(f"Ошибка: Неверный формат JSON в файле {filepath}.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


# Пример использования:
filepath = "lab.json"  # Замените на путь к вашему файлу
version_prefix_to_find = "1"  # Замените на нужный префикс версии
analyze_json(filepath, version_prefix_to_find)


