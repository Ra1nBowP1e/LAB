import os
import subprocess
import shutil

def open_file(filepath):
    """Открывает файл с помощью текстового редактора."""
    try:
        if os.path.exists(filepath):
            subprocess.run(["notepad.exe", filepath])  # Можно заменить notepad.exe на другой редактор
        else:
            print("Файл не найден.")
    except FileNotFoundError:
        print("Текстовый редактор не найден.")
    except Exception as e:
        print(f"Ошибка при открытии файла: {e}")


def delete_item(filepath):
    """Удаляет файл или папку."""
    try:
        if os.path.exists(filepath):
            if os.path.isfile(filepath):
                os.remove(filepath)
                print(f"Файл '{filepath}' удален.")
            elif os.path.isdir(filepath):
                shutil.rmtree(filepath) # Используем rmtree для удаления директорий и их содержимого
                print(f"Папка '{filepath}' удалена.")
            else:
                print("Неизвестный тип файла/папки.")
        else:
            print("Файл/папка не найден.")
    except OSError as e:
        print(f"Ошибка при удалении: {e}")


def copy_item(source, destination):
    """Копирует файл или папку."""
    try:
        if os.path.exists(source):
            if os.path.isfile(source):
                shutil.copy2(source, destination) # copy2 сохраняет метаданные
                print(f"Файл '{source}' скопирован в '{destination}'.")
            elif os.path.isdir(source):
                shutil.copytree(source, destination) # copytree для копирования директорий рекурсивно
                print(f"Папка '{source}' скопирована в '{destination}'.")
            else:
                print("Неизвестный тип файла/папки.")
        else:
            print("Исходный файл/папка не найден.")
    except OSError as e:
        print(f"Ошибка при копировании: {e}")
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")


def main():
    while True:
        print("\nВыберите действие:")
        print("1. Открыть файл")
        print("2. Удалить файл/папку")
        print("3. Копировать файл/папку")
        print("4. Выйти")

        choice = input("Введите номер действия: ")

        if choice == '1':
            filepath = input("Введите путь к файлу: ")
            open_file(filepath)
        elif choice == '2':
            filepath = input("Введите путь к файлу/папке: ")
            delete_item(filepath)
        elif choice == '3':
            source = input("Введите путь к исходному файлу/папке: ")
            destination = input("Введите путь к месту назначения: ")
            copy_item(source, destination)
        elif choice == '4':
            break
        else:
            print("Неверный выбор.")

if __name__ == "__main__":
    main()
