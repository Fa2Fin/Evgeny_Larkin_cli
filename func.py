import os
import shutil


def print_help():
    help_text = """
    Доступные команды:
    - ls                : Показать содержимое текущего каталога.
    - cd <path>        : Перейти в указанный каталог.
    - cp <src> <dst>   : Скопировать файл или каталог.
    - mv <src> <dst>   : Переместить файл или каталог.
    - rm <path>        : Удалить файл или каталог.
    - help             : Показать это сообщение.
    - exit             : Выйти из программы.
    """
    print(help_text)


def list_directory():
    print("Содержимое текущего каталога:")
    for item in os.listdir():
        print(f" - {item}")


def change_directory(path):
    try:
        os.chdir(path)
        print(f"Перешли в каталог: {os.getcwd()}")
    except FileNotFoundError:
        print("Ошибка: Указанный путь не найден.")
    except NotADirectoryError:
        print("Ошибка: Указанный путь не является каталогом.")


def copy_file(src, dst):
    try:
        shutil.copy(src, dst)
        print(f"Скопирован: {src} -> {dst}")
    except FileNotFoundError:
        print("Ошибка: Исходный файл не найден.")
    except Exception as e:
        print(f"Ошибка: {e}")
